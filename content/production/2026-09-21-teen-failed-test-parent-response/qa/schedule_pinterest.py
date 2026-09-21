import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import websocket

ROOT = Path(__file__).parents[1]
QUEUE = ROOT / "pinterest-queue.json"
PORT_FILE = Path(r"C:\Users\wen12\.hermes\browser-owr\DevToolsActivePort")
BASE = "https://nz.pinterest.com"
ACCOUNT = "oldwisdomretold"
BOARD = "Parenting Teens"
seq = 0


def rpc(ws, method, params=None):
    global seq
    seq += 1
    request_id = seq
    ws.send(json.dumps({"id": request_id, "method": method, "params": params or {}}))
    while True:
        response = json.loads(ws.recv())
        if response.get("id") == request_id:
            if "error" in response:
                raise RuntimeError(f"{method}: {response['error']}")
            return response.get("result", {})


def evaluate(ws, expression):
    result = rpc(ws, "Runtime.evaluate", {
        "expression": expression,
        "returnByValue": True,
        "awaitPromise": True,
    })["result"]
    if result.get("subtype") == "error":
        raise RuntimeError(result.get("description", expression))
    return result.get("value")


def trusted_click(ws, expression):
    box = evaluate(ws, f"({expression}).getBoundingClientRect().toJSON()")
    if not box or not box.get("width") or not box.get("height"):
        raise RuntimeError(f"missing/offscreen click target: {expression}")
    x = box["x"] + box["width"] / 2
    y = box["y"] + box["height"] / 2
    for event_type in ("mouseMoved", "mousePressed", "mouseReleased"):
        rpc(ws, "Input.dispatchMouseEvent", {
            "type": event_type,
            "x": x,
            "y": y,
            "button": "left",
            "clickCount": 1,
        })


def set_value(ws, selector, value, prototype):
    actual = evaluate(ws, f"""(() => {{
      const e = document.querySelector({json.dumps(selector)});
      if (!e) throw new Error('missing {selector}');
      const setter = Object.getOwnPropertyDescriptor({prototype}.prototype, 'value').set;
      setter.call(e, {json.dumps(value)});
      e.dispatchEvent(new Event('input', {{bubbles:true}}));
      e.dispatchEvent(new Event('change', {{bubbles:true}}));
      return e.value;
    }})()""")
    if actual != value:
        raise RuntimeError(f"readback failed for {selector}: {actual!r}")


def wait_for(ws, expression, timeout=30, interval=0.5):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            value = evaluate(ws, expression)
            if value:
                return value
        except Exception:
            pass
        time.sleep(interval)
    raise TimeoutError(expression)


def fresh_page(port):
    version = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version", timeout=10))
    browser_ws = websocket.create_connection(version["webSocketDebuggerUrl"], suppress_origin=True, timeout=30)
    target_id = rpc(browser_ws, "Target.createTarget", {"url": f"{BASE}/business/hub/"})["targetId"]
    rpc(browser_ws, "Target.activateTarget", {"targetId": target_id})
    browser_ws.close()
    time.sleep(7)
    pages = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=10))
    target = next(p for p in pages if p.get("id") == target_id)
    return target_id, websocket.create_connection(target["webSocketDebuggerUrl"], suppress_origin=True, timeout=40)


def save_queue(queue):
    QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def schedule_one(port, queue, pin):
    target_id, ws = fresh_page(port)
    try:
        profile = wait_for(ws, "document.querySelector('a[aria-label=\"Your profile\"]')?.href || ''")
        if f"/{ACCOUNT}/" not in profile:
            raise RuntimeError(f"wrong Pinterest identity: {profile}")

        rpc(ws, "Page.navigate", {"url": f"{BASE}/pin-builder/"})
        wait_for(ws, "!!document.querySelector('input[aria-label=\"File upload\"],input[type=file]')", timeout=30)
        document = rpc(ws, "DOM.getDocument", {"depth": -1, "pierce": True})["root"]["nodeId"]
        file_node = rpc(ws, "DOM.querySelector", {
            "nodeId": document,
            "selector": 'input[aria-label="File upload"],input[type=file]',
        })["nodeId"]
        asset = str((ROOT / pin["asset"]).resolve())
        rpc(ws, "DOM.setFileInputFiles", {"nodeId": file_node, "files": [asset]})
        wait_for(ws, "!!document.querySelector('[data-test-id=\"board-dropdown-select-button\"]')", timeout=35)
        time.sleep(3)

        selected_board = evaluate(ws, "document.querySelector('[data-test-id=\"board-dropdown-select-button\"]').innerText.trim()")
        if selected_board != BOARD:
            trusted_click(ws, "document.querySelector('[data-test-id=\"board-dropdown-select-button\"]')")
            wait_for(ws, f"!!document.querySelector('[data-test-id={json.dumps('board-row-' + BOARD)}]')")
            trusted_click(ws, f"document.querySelector('[data-test-id={json.dumps('board-row-' + BOARD)}]').closest('[role=button]')")
            time.sleep(1)
            selected_board = evaluate(ws, "document.querySelector('[data-test-id=\"board-dropdown-select-button\"]').innerText.trim()")
        if selected_board != BOARD:
            raise RuntimeError(f"board mismatch: {selected_board}")

        evaluate(ws, "document.querySelector('input[value=publish-later]').click()")
        wait_for(ws, "document.querySelector('input[value=publish-later]').checked && !!document.querySelector('input[placeholder=\"DD/MM/YYYY\"]') && !!document.querySelector('input[placeholder=Time]')")

        date_value = "/".join(reversed(pin["scheduled_date"].split("-")))
        hour, minute = pin["scheduled_time"].split(":")
        time_value = f"{(int(hour) % 12 or 12):02d}:{minute} {'AM' if int(hour) < 12 else 'PM'}"
        set_value(ws, 'input[placeholder="DD/MM/YYYY"]', date_value, "HTMLInputElement")
        rpc(ws, "Input.dispatchKeyEvent", {"type": "keyDown", "windowsVirtualKeyCode": 27})
        rpc(ws, "Input.dispatchKeyEvent", {"type": "keyUp", "windowsVirtualKeyCode": 27})
        time.sleep(1)
        trusted_click(ws, "document.querySelector('input[placeholder=Time]')")
        wait_for(ws, f"[...document.querySelectorAll('[data-test-id=time-field-option]')].some(e => e.innerText?.trim() === {json.dumps(time_value)})")
        option = f"[...document.querySelectorAll('[data-test-id=time-field-option]')].find(e => e.innerText?.trim() === {json.dumps(time_value)})"
        evaluate(ws, f"({option}).scrollIntoView({{block:'center'}})")
        time.sleep(0.5)
        trusted_click(ws, option)
        time.sleep(1)

        set_value(ws, 'textarea[placeholder="Add your title"]', pin["title"], "HTMLTextAreaElement")
        set_value(ws, 'textarea[placeholder="Add a destination link"]', pin["url"], "HTMLTextAreaElement")
        alt_selector = 'textarea[placeholder="Explain what people can see in the Pin"]'
        if evaluate(ws, f"!!document.querySelector({json.dumps(alt_selector)})"):
            set_value(ws, alt_selector, pin["alt_text"], "HTMLTextAreaElement")

        description_selector = '[contenteditable=true][aria-label="Tell everyone what your Pin is about"]'
        trusted_click(ws, f"document.querySelector({json.dumps(description_selector)})")
        rpc(ws, "Input.insertText", {"text": pin["description"]})
        rpc(ws, "Input.dispatchKeyEvent", {"type": "keyDown", "windowsVirtualKeyCode": 9})
        rpc(ws, "Input.dispatchKeyEvent", {"type": "keyUp", "windowsVirtualKeyCode": 9})
        time.sleep(1)

        ai_selector = 'input[id^="pin-draft-ai-disclosure-"]:not([id$="synthetic-performer"])'
        synthetic_selector = 'input[id$="synthetic-performer"]'
        desired = [(ai_selector, True), (synthetic_selector, bool(pin["synthetic_person"]))]
        for selector, wanted in desired:
            checked = evaluate(ws, f"document.querySelector({json.dumps(selector)}).checked")
            if checked != wanted:
                evaluate(ws, f"document.querySelector({json.dumps(selector)}).click()")

        state = evaluate(ws, """(() => ({
          profile: document.querySelector('a[aria-label="Your profile"]')?.href || '',
          board: document.querySelector('[data-test-id="board-dropdown-select-button"]')?.innerText.trim(),
          title: document.querySelector('textarea[placeholder="Add your title"]')?.value,
          link: document.querySelector('textarea[placeholder="Add a destination link"]')?.value,
          alt: document.querySelector('textarea[placeholder="Explain what people can see in the Pin"]')?.value || null,
          description: document.querySelector('[aria-label="Tell everyone what your Pin is about"]')?.innerText,
          date: document.querySelector('input[placeholder="DD/MM/YYYY"]')?.value,
          time: document.querySelector('input[placeholder=Time]')?.value,
          later: document.querySelector('input[value=publish-later]')?.checked,
          checks: [...document.querySelectorAll('input[type=checkbox]')].map(e => e.checked),
          saveDisabled: document.querySelector('[data-test-id="board-dropdown-save-button"]')?.getAttribute('aria-disabled')
        }))()""")
        expected_checks = [True, bool(pin["synthetic_person"])]
        failures = []
        for key, expected in {
            "board": BOARD,
            "title": pin["title"],
            "link": pin["url"],
            "description": pin["description"],
            "date": date_value,
            "time": time_value,
            "later": True,
            "checks": expected_checks,
            "saveDisabled": "false",
        }.items():
            if state.get(key) != expected:
                failures.append(f"{key}={state.get(key)!r} expected {expected!r}")
        if f"/{ACCOUNT}/" not in state["profile"]:
            failures.append(f"profile={state['profile']!r}")
        if state.get("alt") is not None and state["alt"] != pin["alt_text"]:
            failures.append("alt text mismatch")
        if failures:
            raise RuntimeError("preflight failed: " + "; ".join(failures))

        trusted_click(ws, "document.querySelector('[data-test-id=\"board-dropdown-save-button\"]')")
        deadline = time.time() + 45
        while time.time() < deadline:
            body = evaluate(ws, "document.body.innerText") or ""
            if "You created a Pin" in body or "scheduled" in body.lower():
                break
            time.sleep(1)
        else:
            raise RuntimeError("no Pinterest confirmation")

        rpc(ws, "Page.navigate", {"url": f"{BASE}/{ACCOUNT}/scheduled-pins/"})
        wait_for(ws, f"document.body.innerText.includes({json.dumps(pin['title'])})", timeout=35)
        card = evaluate(ws, f"""(() => {{
          const a = [...document.querySelectorAll('a[href*="/scheduled-pin/"]')]
            .find(a => (a.innerText || '').includes({json.dumps(pin['title'])}));
          return a ? {{href:a.href,text:a.innerText.trim().replace(/\\s+/g,' ')}} : null;
        }})()""")
        if not card:
            raise RuntimeError("provider card missing")
        year, month, day = pin["scheduled_date"].split("-")
        provider_date = f"{int(day)}/{int(month)}"
        if provider_date not in card["text"]:
            raise RuntimeError(f"provider date mismatch: {card}")
        if f"{time_value[:-3].lstrip('0')} {time_value[-2:].lower()}" not in card["text"].lower():
            raise RuntimeError(f"provider time mismatch: {card}")

        pin["status"] = "scheduled_ui"
        pin["scheduled_verified_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        pin["scheduled_pin_url"] = card["href"]
        pin["provider_card_text"] = card["text"]
        save_queue(queue)
        print("SCHEDULED_VERIFIED", pin["id"], pin["scheduled_date"], pin["scheduled_time"], card["href"], flush=True)
    finally:
        ws.close()


def final_audit(port, queue):
    _, ws = fresh_page(port)
    try:
        rpc(ws, "Page.navigate", {"url": f"{BASE}/{ACCOUNT}/scheduled-pins/"})
        wait_for(ws, "document.body.innerText.includes('Scheduled Pins')", timeout=35)
        time.sleep(3)
        body = evaluate(ws, "document.body.innerText")
        missing = [pin["title"] for pin in queue["pins"] if pin["title"] not in body]
        if missing:
            raise RuntimeError(f"final provider audit missing: {missing}")
        cards = json.loads(evaluate(ws, "JSON.stringify([...document.querySelectorAll('a[href*=\"/scheduled-pin/\"]')].map(a=>({href:a.href,text:(a.innerText||'').trim().replace(/\\s+/g,' ')})))"))
        report = {
            "verified_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "account": ACCOUNT,
            "scheduled_count": len(cards),
            "all_campaign_titles_present": not missing,
            "campaign_cards": [c for c in cards if any(p["title"] in c["text"] for p in queue["pins"])],
        }
        (ROOT / "qa" / "pinterest-schedule-verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("FINAL_PROVIDER_AUDIT", json.dumps(report, ensure_ascii=False), flush=True)
    finally:
        ws.close()


def main():
    port = int(PORT_FILE.read_text(encoding="utf-8").splitlines()[0])
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))
    for pin in queue["pins"]:
        if pin.get("status") != "scheduled_ui":
            schedule_one(port, queue, pin)
    final_audit(port, queue)


if __name__ == "__main__":
    main()
