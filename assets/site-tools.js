(function () {
  'use strict';

  var GTRANSLATE_SCRIPT_ID = 'site-gtranslate-script';
  var GTRANSLATE_SCRIPT_URL = 'https://cdn.gtranslate.net/widgets/latest/dropdown.js';
  var BACK_TO_TOP_THRESHOLD = 0.7;

  function createLanguageTool() {
    if (document.querySelector('[data-site-language-tool]')) {
      return;
    }

    var tool = document.createElement('details');
    tool.className = 'site-language-tool';
    tool.dataset.siteLanguageTool = '';

    var summary = document.createElement('summary');
    summary.className = 'site-language-summary';
    summary.innerHTML = '<span class="site-language-icon" aria-hidden="true">&#127760;</span><span>Language</span>';

    var panel = document.createElement('div');
    panel.className = 'site-language-panel';

    var heading = document.createElement('p');
    heading.className = 'site-language-heading';
    heading.textContent = 'Choose your language';

    var wrapper = document.createElement('div');
    wrapper.className = 'gtranslate_wrapper';

    var note = document.createElement('p');
    note.className = 'site-language-note';
    note.textContent = 'Machine translation may contain errors.';

    var status = document.createElement('p');
    status.className = 'site-language-status';
    status.setAttribute('role', 'status');
    status.setAttribute('aria-live', 'polite');
    status.textContent = 'Open to load language choices.';

    panel.appendChild(heading);
    panel.appendChild(wrapper);
    panel.appendChild(note);
    panel.appendChild(status);
    tool.appendChild(summary);
    tool.appendChild(panel);
    document.body.appendChild(tool);

    var loadState = 'idle';

    function loadGTranslate() {
      if (loadState === 'loading' || loadState === 'ready') {
        return;
      }

      loadState = 'loading';
      tool.classList.add('is-loading');
      tool.classList.remove('has-error');
      status.textContent = 'Loading language choices…';

      window.gtranslateSettings = {
        default_language: 'en',
        native_language_names: true,
        detect_browser_language: false,
        wrapper_selector: '.site-language-tool .gtranslate_wrapper'
      };

      var existingScript = document.getElementById(GTRANSLATE_SCRIPT_ID);
      if (existingScript) {
        existingScript.remove();
      }

      var script = document.createElement('script');
      script.id = GTRANSLATE_SCRIPT_ID;
      script.src = GTRANSLATE_SCRIPT_URL;
      script.async = true;
      script.onload = function () {
        loadState = 'ready';
        tool.classList.remove('is-loading');
        status.textContent = 'Select a language.';
      };
      script.onerror = function () {
        loadState = 'error';
        tool.classList.remove('is-loading');
        tool.classList.add('has-error');
        status.textContent = 'Language choices could not load. Close and reopen to try again.';
        script.remove();
      };

      document.head.appendChild(script);
    }

    tool.addEventListener('toggle', function () {
      if (tool.open) {
        loadGTranslate();
      }
    });
  }

  function isArticlePage() {
    var type = document.querySelector('meta[property="og:type"]');
    var isArticle = type && type.getAttribute('content') && type.getAttribute('content').toLowerCase() === 'article';
    return Boolean(isArticle && document.querySelector('main#article, article'));
  }

  function createBackToTopTool() {
    if (!isArticlePage()) {
      return;
    }

    if (!document.body.id) {
      document.body.id = 'top';
    }

    var backToTop = null;
    var framePending = false;
    var targetId = document.body.id;

    function ensureBackToTop() {
      if (backToTop) {
        return backToTop;
      }

      backToTop = document.createElement('a');
      backToTop.className = 'site-back-to-top';
      backToTop.href = '#' + encodeURIComponent(targetId);
      backToTop.setAttribute('aria-label', 'Back to top');
      backToTop.setAttribute('title', 'Back to top');
      backToTop.innerHTML = '<span aria-hidden="true">&#8593;</span>';
      backToTop.addEventListener('click', function () {
        window.setTimeout(function () {
          var topLink = document.querySelector('.parent-nav a, .nav a, nav a');
          if (topLink) {
            topLink.focus({ preventScroll: true });
          }
        }, 0);
      });
      backToTop.addEventListener('blur', requestUpdate);
      document.body.appendChild(backToTop);
      return backToTop;
    }

    function updateBackToTop() {
      framePending = false;
      var threshold = Math.max(320, window.innerHeight * BACK_TO_TOP_THRESHOLD);
      var shouldShow = window.scrollY > threshold;

      if (shouldShow) {
        var control = ensureBackToTop();
        control.classList.add('is-visible');
        control.removeAttribute('aria-hidden');
        control.removeAttribute('tabindex');
      } else if (backToTop && document.activeElement !== backToTop) {
        backToTop.classList.remove('is-visible');
        backToTop.setAttribute('aria-hidden', 'true');
        backToTop.setAttribute('tabindex', '-1');
      }
    }

    function requestUpdate() {
      if (!framePending) {
        framePending = true;
        window.requestAnimationFrame(updateBackToTop);
      }
    }

    window.addEventListener('scroll', requestUpdate, { passive: true });
    window.addEventListener('resize', requestUpdate);
    updateBackToTop();
  }

  function initialiseSiteTools() {
    createLanguageTool();
    createBackToTopTool();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialiseSiteTools, { once: true });
  } else {
    initialiseSiteTools();
  }
}());
