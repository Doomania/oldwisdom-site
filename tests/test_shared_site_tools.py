import unittest
from pathlib import Path


class SharedSiteToolsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]

    def public_html(self):
        return sorted(
            path
            for path in self.root.rglob("*.html")
            if "templates" not in path.relative_to(self.root).parts
        )

    def test_every_public_page_loads_shared_tools_locally(self):
        pages = self.public_html()
        self.assertGreater(len(pages), 5)
        for path in pages:
            with self.subTest(page=path.relative_to(self.root)):
                content = path.read_text(encoding="utf-8")
                self.assertRegex(content, r'<link[^>]+href="/assets/site-tools\.css"')
                self.assertRegex(content, r'<script[^>]+src="/assets/site-tools\.js"[^>]*>')
                self.assertNotIn("cdn.gtranslate.net", content)

    def test_translator_is_on_demand_and_does_not_auto_switch(self):
        script = (self.root / "assets" / "site-tools.js").read_text(encoding="utf-8")
        self.assertIn("tool.addEventListener('toggle'", script)
        self.assertIn("https://cdn.gtranslate.net/widgets/latest/dropdown.js", script)
        self.assertIn("detect_browser_language: false", script)
        self.assertIn("Machine translation may contain errors.", script)
        self.assertIn("site-back-to-top", script)
        self.assertIn("topLink.focus({ preventScroll: true });", script)

    def test_blog_navigation_stays_available_while_scrolling(self):
        shared_css = (self.root / "assets" / "parent-hub.css").read_text(encoding="utf-8")
        self.assertRegex(shared_css, r"\.parent-nav\s*\{[^}]*position:sticky")

        for name in ("quiet-kids-and-confidence.html", "signs-of-real-teen-confidence.html"):
            with self.subTest(page=name):
                content = (self.root / "articles" / name).read_text(encoding="utf-8")
                self.assertRegex(content, r"\.nav\s*\{[^}]*position:sticky")
                self.assertIn('<body id="top">', content)

    def test_privacy_policy_discloses_translation_provider(self):
        privacy = (self.root / "privacy.html").read_text(encoding="utf-8")
        self.assertIn("GTranslate", privacy)
        self.assertIn("https://gtranslate.io/privacy-policy", privacy)
        self.assertIn("https://policies.google.com/privacy", privacy)


if __name__ == "__main__":
    unittest.main()
