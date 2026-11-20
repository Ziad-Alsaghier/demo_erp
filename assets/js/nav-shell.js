/**
 * Wise ERP Global Navigation Shell & Enterprise Interactivity Controller
 */

(function () {
  // Screen Registry for Global Navigation & Command Palette
  const SCREENS = [
    // Analytics
    { id: 'executive-dashboard', title: 'Executive Dashboard', titleAr: 'لوحة القيادة التنفيذية', category: 'Analytics', categoryAr: 'التحليلات', icon: 'monitoring', path: 'analytics/executive-dashboard.html' },
    { id: 'reports-center', title: 'Reports Center', titleAr: 'مركز التقارير الموحد', category: 'Analytics', categoryAr: 'التحليلات', icon: 'summarize', path: 'analytics/reports-center.html' },
    
    // Operations & Logistics
    { id: 'products-catalog', title: 'Product Catalog & Price Lists', titleAr: 'دليل الأصناف وقوائم الأسعار', category: 'Operations', categoryAr: 'العمليات', icon: 'category', path: 'operations/products-catalog.html' },
    { id: 'stock-availability', title: 'Stock on Hand & Availability', titleAr: 'المخزون الفعلي والجاهزية', category: 'Operations', categoryAr: 'العمليات', icon: 'warehouse', path: 'operations/stock-availability.html' },
    { id: 'goods-receipts-grn', title: 'Goods Receipts & GRN', titleAr: 'أذون استلام البضائع GRN', category: 'Operations', categoryAr: 'العمليات', icon: 'receipt_long', path: 'operations/goods-receipts-grn.html' },
    { id: 'inter-warehouse-transfers', title: 'Inter-Warehouse Transfers', titleAr: 'التحويلات بين المستودعات', category: 'Operations', categoryAr: 'العمليات', icon: 'move_up', path: 'operations/inter-warehouse-transfers.html' },
    { id: 'barcode-shelf-labels', title: 'Barcode & Shelf Labels Print Center', titleAr: 'مركز طباعة الباركود والملصقات', category: 'Operations', categoryAr: 'العمليات', icon: 'barcode_scanner', path: 'operations/barcode-shelf-labels.html' },
    
    // Sales & CRM
    { id: 'sales-pipeline-kanban', title: 'Sales Pipeline & Kanban', titleAr: 'مسار المبيعات ولوحة كانبان', category: 'Sales', categoryAr: 'المبيعات', icon: 'view_kanban', path: 'sales/sales-pipeline-kanban.html' },
    { id: 'sales-quotation', title: 'Sales Quotation Form', titleAr: 'نموذج عروض أسعار المبيعات', category: 'Sales', categoryAr: 'المبيعات', icon: 'request_quote', path: 'sales/sales-quotation.html' },
    { id: 'customer-360', title: 'Customer 360 Dossier', titleAr: 'ملف العميل المتكامل 360°', category: 'Sales', categoryAr: 'المبيعات', icon: 'contacts', path: 'sales/customer-360.html' },
    
    // Finance & Accounting
    { id: 'chart-of-accounts', title: 'Chart of Accounts (COA)', titleAr: 'دليل الحسابات الشجري', category: 'Finance', categoryAr: 'المالية', icon: 'table_chart', path: 'finance/chart-of-accounts.html' },
    { id: 'journal-entries', title: 'Journal Entries & Vouchers', titleAr: 'قيود اليومية وسندات الصرف', category: 'Finance', categoryAr: 'المالية', icon: 'menu_book', path: 'finance/journal-entries.html' },
    { id: 'treasury-cheques', title: 'Treasury & Cheques Portfolio', titleAr: 'الخزينة ومحفظة الشيكات', category: 'Finance', categoryAr: 'المالية', icon: 'savings', path: 'finance/treasury-cheques.html' },
    
    // People & HR
    { id: 'daily-attendance-board', title: 'Daily Attendance Board', titleAr: 'لوحة الحضور والانصراف اليومية', category: 'People', categoryAr: 'الموارد البشرية', icon: 'how_to_reg', path: 'hr/daily-attendance-board.html' },
    { id: 'my-attendance-mobile', title: 'My Attendance Mobile Portal', titleAr: 'سجل حضوري الذكي (موبايل)', category: 'People', categoryAr: 'الموارد البشرية', icon: 'smartphone', path: 'hr/my-attendance-mobile.html' },
    
    // Administration & Security
    { id: 'security-permission-matrix', title: 'Security Permission Matrix', titleAr: 'مصفوفة صلاحيات المستخدمين', category: 'Security', categoryAr: 'الأمان', icon: 'security', path: 'security/security-permission-matrix.html' },
    { id: 'field-level-rules', title: 'Field-Level Masking & Rules', titleAr: 'قواعد حجب وتشفير الحقول', category: 'Security', categoryAr: 'الأمان', icon: 'vpn_key', path: 'security/field-level-rules.html' },
    
    // Auth
    { id: 'corporate-sso-login', title: 'Corporate SSO Login', titleAr: 'بوابة الدخول الموحد SSO', category: 'Auth', categoryAr: 'الدخول', icon: 'login', path: 'auth/corporate-sso-login.html' },
    { id: 'two-factor-authentication', title: 'Two-Factor Authentication (MFA)', titleAr: 'المصادقة الثنائية والتحقق', category: 'Auth', categoryAr: 'الدخول', icon: 'verified_user', path: 'auth/two-factor-authentication.html' }
  ];

  // Quick Actions for Command Palette
  const ACTIONS = [
    { id: 'act-new-quotation', title: 'Create New Quotation', titleAr: 'إنشاء عرض سعر جديد', icon: 'add_circle', path: 'sales/sales-quotation.html' },
    { id: 'act-new-grn', title: 'Record Goods Receipt (GRN)', titleAr: 'تسجيل إذن استلام بضائع', icon: 'receipt_long', path: 'operations/goods-receipts-grn.html' },
    { id: 'act-new-transfer', title: 'Initiate Stock Transfer', titleAr: 'بدء تحويل مخزني بين المستودعات', icon: 'move_up', path: 'operations/inter-warehouse-transfers.html' },
    { id: 'act-print-labels', title: 'Print Shelf & Barcode Labels', titleAr: 'طباعة ملصقات الباركود والأرفف', icon: 'print', path: 'operations/barcode-shelf-labels.html' },
    { id: 'act-journal-entry', title: 'Create Journal Voucher', titleAr: 'إضافة قيد يومية محاسبي', icon: 'edit_document', path: 'finance/journal-entries.html' },
    { id: 'act-logout', title: 'Log Out of Wise ERP', titleAr: 'تسجيل الخروج من المنظومة', icon: 'logout', path: 'auth/corporate-sso-login.html' }
  ];

  // Helper to resolve relative path based on current directory depth
  function resolveRelativePath(targetPath) {
    const loc = window.location.pathname;
    const isRoot = !loc.includes('/analytics/') && 
                   !loc.includes('/operations/') && 
                   !loc.includes('/sales/') && 
                   !loc.includes('/finance/') && 
                   !loc.includes('/hr/') && 
                   !loc.includes('/security/') && 
                   !loc.includes('/auth/');
    return isRoot ? targetPath : '../' + targetPath;
  }

  // Toast Notification Service
  function showToast({ title, message, type = 'info', duration = 3500 }) {
    let container = document.getElementById('wise-toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'wise-toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `wise-toast toast-${type}`;

    let iconName = 'info';
    if (type === 'success') iconName = 'check_circle';
    if (type === 'warning') iconName = 'warning';
    if (type === 'error') iconName = 'error';

    toast.innerHTML = `
      <span class="material-symbols-outlined toast-icon text-[22px] flex-shrink-0">${iconName}</span>
      <div class="flex flex-col flex-1 gap-0.5">
        <span class="font-title-md text-[14px] font-bold text-on-surface">${title || 'Notification'}</span>
        <span class="font-body-sm text-[12px] text-on-surface-variant leading-snug">${message || ''}</span>
      </div>
      <button class="toast-close text-outline hover:text-on-surface transition-colors">
        <span class="material-symbols-outlined text-[16px]">close</span>
      </button>
    `;

    toast.querySelector('.toast-close').addEventListener('click', () => {
      dismissToast(toast);
    });

    container.appendChild(toast);

    if (duration > 0) {
      setTimeout(() => {
        dismissToast(toast);
      }, duration);
    }
  }

  function dismissToast(toast) {
    toast.classList.add('toast-hiding');
    setTimeout(() => {
      if (toast.parentNode) toast.parentNode.removeChild(toast);
    }, 300);
  }

  // Command Palette Builder
  function initCommandPalette() {
    const palette = document.createElement('div');
    palette.id = 'wise-command-palette';
    palette.innerHTML = `
      <div class="cmd-box">
        <div class="p-4 border-b border-white/10 flex items-center gap-3">
          <span class="material-symbols-outlined text-secondary text-[22px]">search</span>
          <input type="text" id="cmd-input" class="w-full bg-transparent text-on-surface placeholder:text-outline text-base focus:outline-none" placeholder="Type a screen or command (e.g., Quotation, GRN, Stock)..." />
          <span class="px-2 py-0.5 rounded bg-surface-container-high border border-white/10 text-xs text-outline">ESC</span>
        </div>
        <div class="max-h-[380px] overflow-y-auto p-2 space-y-1" id="cmd-results"></div>
        <div class="p-3 bg-surface-container-lowest/80 border-t border-white/5 flex items-center justify-between text-xs text-outline">
          <span data-i18n="cmd_hint">Use ↑↓ to navigate, Enter to select, ESC to dismiss</span>
          <span class="text-secondary font-semibold">Wise ERP Enterprise</span>
        </div>
      </div>
    `;
    document.body.appendChild(palette);

    const input = palette.querySelector('#cmd-input');
    const resultsContainer = palette.querySelector('#cmd-results');
    let selectedIndex = 0;

    function renderResults(filterText = '') {
      const lang = window.WiseI18n ? window.WiseI18n.getLanguage() : 'en';
      const isAr = lang === 'ar';
      const query = filterText.toLowerCase().trim();

      const matchedScreens = SCREENS.filter(s => 
        !query || 
        s.title.toLowerCase().includes(query) || 
        (s.titleAr && s.titleAr.includes(query)) ||
        s.category.toLowerCase().includes(query) ||
        (s.categoryAr && s.categoryAr.includes(query))
      );

      const matchedActions = ACTIONS.filter(a => 
        !query || 
        a.title.toLowerCase().includes(query) || 
        (a.titleAr && a.titleAr.includes(query))
      );

      resultsContainer.innerHTML = '';

      if (matchedScreens.length === 0 && matchedActions.length === 0) {
        resultsContainer.innerHTML = `
          <div class="py-8 text-center text-outline text-sm">
            <span class="material-symbols-outlined text-[32px] mb-1 opacity-50 block">search_off</span>
            <span>${isAr ? 'لم يتم العثور على نتائج' : 'No matching screens or actions found'}</span>
          </div>
        `;
        return;
      }

      // Actions first
      if (matchedActions.length > 0) {
        const actionHeader = document.createElement('div');
        actionHeader.className = 'px-3 py-1.5 text-[11px] font-bold text-secondary uppercase tracking-wider';
        actionHeader.textContent = isAr ? 'إجراءات سريعة' : 'Quick Actions';
        resultsContainer.appendChild(actionHeader);

        matchedActions.forEach((act, idx) => {
          const item = document.createElement('a');
          item.href = resolveRelativePath(act.path);
          item.className = 'cmd-item';
          item.setAttribute('data-cmd-idx', idx);
          item.innerHTML = `
            <div class="flex items-center gap-3">
              <span class="material-symbols-outlined text-secondary text-[20px]">${act.icon}</span>
              <span class="font-medium text-sm">${isAr ? act.titleAr : act.title}</span>
            </div>
            <span class="text-xs text-outline bg-surface-container-high px-2 py-0.5 rounded">Action</span>
          `;
          resultsContainer.appendChild(item);
        });
      }

      // Screens
      if (matchedScreens.length > 0) {
        const screenHeader = document.createElement('div');
        screenHeader.className = 'px-3 py-1.5 text-[11px] font-bold text-outline uppercase tracking-wider mt-2';
        screenHeader.textContent = isAr ? 'شاشات المنظومة' : 'System Screens';
        resultsContainer.appendChild(screenHeader);

        matchedScreens.forEach((scr, idx) => {
          const item = document.createElement('a');
          item.href = resolveRelativePath(scr.path);
          item.className = 'cmd-item';
          item.innerHTML = `
            <div class="flex items-center gap-3">
              <span class="material-symbols-outlined text-primary text-[20px]">${scr.icon}</span>
              <div class="flex flex-col">
                <span class="font-medium text-sm text-on-surface">${isAr ? scr.titleAr : scr.title}</span>
                <span class="text-[11px] text-outline">${isAr ? scr.categoryAr : scr.category}</span>
              </div>
            </div>
            <span class="material-symbols-outlined text-outline text-[18px]">arrow_forward</span>
          `;
          resultsContainer.appendChild(item);
        });
      }

      updateSelection(0);
    }

    function updateSelection(newIdx) {
      const items = resultsContainer.querySelectorAll('.cmd-item');
      if (items.length === 0) return;
      if (newIdx < 0) newIdx = items.length - 1;
      if (newIdx >= items.length) newIdx = 0;
      selectedIndex = newIdx;

      items.forEach((it, i) => {
        if (i === selectedIndex) {
          it.classList.add('selected');
          it.scrollIntoView({ block: 'nearest' });
        } else {
          it.classList.remove('selected');
        }
      });
    }

    input.addEventListener('input', (e) => {
      renderResults(e.target.value);
    });

    input.addEventListener('keydown', (e) => {
      const items = resultsContainer.querySelectorAll('.cmd-item');
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        updateSelection(selectedIndex + 1);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        updateSelection(selectedIndex - 1);
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (items[selectedIndex]) {
          items[selectedIndex].click();
        }
      } else if (e.key === 'Escape') {
        closePalette();
      }
    });

    palette.addEventListener('click', (e) => {
      if (e.target === palette) closePalette();
    });

    function openPalette() {
      palette.classList.add('active');
      renderResults('');
      setTimeout(() => input.focus(), 50);
    }

    function closePalette() {
      palette.classList.remove('active');
      input.value = '';
    }

    // Keyboard trigger Ctrl+K / Cmd+K
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (palette.classList.contains('active')) {
          closePalette();
        } else {
          openPalette();
        }
      } else if (e.key === 'Escape' && palette.classList.contains('active')) {
        closePalette();
      }
    });

    // Delegate clicks on search bar in top header
    document.addEventListener('click', (e) => {
      const searchBox = e.target.closest('.header-search-wrap') || e.target.closest('[data-action="open-cmd"]');
      if (searchBox && !palette.classList.contains('active')) {
        e.preventDefault();
        openPalette();
      }
    });
  }

  // Sidebar Link Active State & Cross Linking Fixer
  function initSidebarAndLinks() {
    const curPath = window.location.pathname.replace(/\\/g, '/');
    
    // Find matching screen in registry
    const currentScreen = SCREENS.find(s => curPath.endsWith(s.path) || curPath.endsWith(s.id + '.html'));

    document.querySelectorAll('aside nav a').forEach(link => {
      const href = link.getAttribute('href');
      const dataPath = link.getAttribute('data-path');

      // Check if this link corresponds to current screen
      const isCurrent = currentScreen && (
        (dataPath && dataPath.includes(currentScreen.id)) ||
        (href && href.includes(currentScreen.id))
      );

      if (isCurrent) {
        link.setAttribute('aria-current', 'page');
        link.className = 'flex items-center gap-3 px-3 py-2 rounded-lg transition-all bg-gradient-to-r from-secondary/20 to-primary-container/10 text-secondary border-l-2 border-secondary font-semibold shadow-[inset_0_1px_0_rgba(255,255,255,0.15)]';
      } else if (link.getAttribute('aria-current') !== 'page') {
        link.className = 'flex items-center gap-3 px-3 py-2 rounded-lg font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-all';
      }
    });
  }

  // Bind Common Action Triggers
  function initCommonInteractions() {
    // EGP / USD Currency switcher
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('#btn-curr-egp, #btn-curr-usd, [data-currency-btn]');
      if (btn) {
        const isEgp = btn.id === 'btn-curr-egp' || btn.getAttribute('data-currency-btn') === 'egp';
        const parent = btn.parentElement;
        if (parent) {
          parent.querySelectorAll('button').forEach(b => {
            b.className = 'px-3 py-1 rounded-lg font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all';
          });
        }
        btn.className = 'px-3 py-1 rounded-lg font-label-md text-label-md font-semibold bg-secondary-container text-on-secondary-container shadow-sm transition-all';
        showToast({
          title: 'Currency Toggled',
          message: `Display currency converted to ${isEgp ? 'EGP (Egyptian Pound)' : 'USD (US Dollar)'}`,
          type: 'info'
        });
      }
    });

    // Operating Hub selector
    document.addEventListener('change', (e) => {
      const select = e.target.closest('header select');
      if (select) {
        showToast({
          title: 'Operating Hub Switched',
          message: `Active operational scope changed to ${select.value}`,
          type: 'success'
        });
      }
    });

    // General simulation toasts for action buttons
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('button');
      if (!btn) return;
      const text = (btn.textContent || '').trim().toLowerCase();

      if (text.includes('export') || text.includes('تصدير')) {
        showToast({
          title: 'Export Initiated',
          message: 'Exporting tabular dataset to Excel/PDF format...',
          type: 'info'
        });
      } else if (text.includes('print') || text.includes('طباعة')) {
        showToast({
          title: 'Print Center',
          message: 'Spooling barcode labels to thermal network printer (Zebra ZD421)...',
          type: 'success'
        });
      } else if (text.includes('approve') || text.includes('اعتماد')) {
        showToast({
          title: 'Transaction Approved',
          message: 'Voucher posted to General Ledger and inventory balance committed.',
          type: 'success'
        });
      }
    });
  }

  // Initialization
  document.addEventListener('DOMContentLoaded', () => {
    initCommandPalette();
    initSidebarAndLinks();
    initCommonInteractions();
  });

  window.WiseERP = {
    screens: SCREENS,
    actions: ACTIONS,
    showToast: showToast,
    resolveRelativePath: resolveRelativePath
  };
})();
