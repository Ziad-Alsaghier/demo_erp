/**
 * Wise ERP Dynamic Real-Time i18n & RTL/LTR Localization Engine
 */

(function () {
  const STORAGE_KEY = 'wise_erp_lang';

  function getLanguage() {
    return localStorage.getItem(STORAGE_KEY) || 'en';
  }

  function setLanguage(lang, silent) {
    if (lang !== 'en' && lang !== 'ar') lang = 'en';
    localStorage.setItem(STORAGE_KEY, lang);

    const htmlEl = document.documentElement;
    const bodyEl = document.body;
    const isRtl = lang === 'ar';

    htmlEl.setAttribute('lang', lang);
    htmlEl.setAttribute('dir', isRtl ? 'rtl' : 'ltr');

    if (bodyEl) {
      if (isRtl) {
        bodyEl.classList.add('font-arabic');
      } else {
        bodyEl.classList.remove('font-arabic');
      }
    }

    applyTranslations(lang);
    updateLangButtons(lang);

    window.dispatchEvent(new CustomEvent('wise:languageChanged', { detail: { lang, isRtl } }));

    if (!silent && window.WiseERP && window.WiseERP.showToast) {
      const msg = window.WISE_TRANSLATIONS && window.WISE_TRANSLATIONS[lang]
        ? window.WISE_TRANSLATIONS[lang].toast_lang_switched
        : (isRtl ? 'تم تغيير اللغة إلى العربية' : 'Switched language to English');
      window.WiseERP.showToast({
        title: isRtl ? 'تغيير اللغة' : 'Language Changed',
        message: msg,
        type: 'info'
      });
    }
  }

  function applyTranslations(lang) {
    if (!window.WISE_TRANSLATIONS || !window.WISE_TRANSLATIONS[lang]) return;
    const dict = window.WISE_TRANSLATIONS[lang];

    // Standard text elements
    document.querySelectorAll('[data-i18n]').forEach((el) => {
      const key = el.getAttribute('data-i18n');
      if (dict[key]) {
        // If element has a child icon, preserve it
        const icon = el.querySelector('.material-symbols-outlined');
        if (icon) {
          const iconClone = icon.cloneNode(true);
          el.textContent = ' ' + dict[key];
          el.prepend(iconClone);
        } else {
          el.textContent = dict[key];
        }
      }
    });

    // Inputs placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach((el) => {
      const key = el.getAttribute('data-i18n-placeholder');
      if (dict[key]) {
        el.setAttribute('placeholder', dict[key]);
      }
    });

    // Titles / Tooltips
    document.querySelectorAll('[data-i18n-title]').forEach((el) => {
      const key = el.getAttribute('data-i18n-title');
      if (dict[key]) {
        el.setAttribute('title', dict[key]);
      }
    });
  }

  function updateLangButtons(lang) {
    document.querySelectorAll('[data-lang-btn]').forEach((btn) => {
      const targetLang = btn.getAttribute('data-lang-btn');
      if (targetLang === lang) {
        btn.className = 'px-2 py-0.5 rounded font-label-sm text-label-sm font-semibold bg-secondary-container text-on-secondary-container transition-all shadow-sm';
      } else {
        btn.className = 'px-2 py-0.5 rounded font-label-sm text-label-sm text-on-surface-variant hover:text-on-surface transition-all';
      }
    });
  }

  // Auto-init upon DOMContentLoaded
  document.addEventListener('DOMContentLoaded', function () {
    const initialLang = getLanguage();
    setLanguage(initialLang, true);

    // Bind click events on any language switcher buttons
    document.addEventListener('click', function (e) {
      const target = e.target.closest('[data-lang-btn]');
      if (target) {
        e.preventDefault();
        const selectedLang = target.getAttribute('data-lang-btn');
        setLanguage(selectedLang);
      }
    });
  });

  window.WiseI18n = {
    getLanguage: getLanguage,
    setLanguage: setLanguage,
    applyTranslations: applyTranslations
  };
})();
