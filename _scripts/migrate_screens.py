import os
import re

SCREEN_CONFIGS = [
    # (source_folder, dest_rel_path, screen_id, title_en, title_ar, i18n_key)
    ('corporate_sso_login_s_auth_login', 'auth/corporate-sso-login.html', 'corporate-sso-login', 'Corporate SSO Login', 'بوابة الدخول الموحد SSO', 'nav_sso_gateway'),
    ('two_factor_authentication_s_auth_mfa', 'auth/two-factor-authentication.html', 'two-factor-authentication', 'Two-Factor Authentication', 'المصادقة الثنائية والتحقق', 'nav_mfa_verification'),
    ('executive_dashboard_s_dash_exec', 'analytics/executive-dashboard.html', 'executive-dashboard', 'Executive Dashboard', 'لوحة القيادة التنفيذية', 'nav_executive_dashboard'),
    ('reports_center_s_reports_center', 'analytics/reports-center.html', 'reports-center', 'Reports Center', 'مركز التقارير الموحد', 'nav_reports_center'),
    ('products_catalog_price_lists_s_prd_list', 'operations/products-catalog.html', 'products-catalog', 'Product Catalog & Price Lists', 'دليل الأصناف وقوائم الأسعار', 'nav_product_catalog'),
    ('stock_on_hand_availability_s_inv_stock', 'operations/stock-availability.html', 'stock-availability', 'Stock on Hand & Availability', 'المخزون الفعلي والجاهزية', 'nav_inventory_stock'),
    ('goods_receipts_grn_s_inv_receipt', 'operations/goods-receipts-grn.html', 'goods-receipts-grn', 'Goods Receipts & GRN', 'أذون استلام البضائع GRN', 'nav_grn_receipts'),
    ('inter_warehouse_transfers_s_inv_transfer', 'operations/inter-warehouse-transfers.html', 'inter-warehouse-transfers', 'Inter-Warehouse Transfers', 'التحويلات بين المستودعات', 'nav_transfers'),
    ('barcode_shelf_label_print_center_s_prd_labels', 'operations/barcode-shelf-labels.html', 'barcode-shelf-labels', 'Barcode & Shelf Labels Print Center', 'مركز طباعة الباركود والملصقات', 'nav_barcode_labels'),
    ('sales_pipeline_kanban_s_sal_kanban', 'sales/sales-pipeline-kanban.html', 'sales-pipeline-kanban', 'Sales Pipeline & Kanban', 'مسار المبيعات ولوحة كانبان', 'nav_pipeline_kanban'),
    ('sales_quotation_form_s_sal_quotation', 'sales/sales-quotation.html', 'sales-quotation', 'Sales Quotation Form', 'نموذج عروض أسعار المبيعات', 'nav_quotations'),
    ('customer_360_s_cus_360', 'sales/customer-360.html', 'customer-360', 'Customer 360 Dossier', 'ملف العميل المتكامل 360°', 'nav_customer_360'),
    ('chart_of_accounts_s_acc_coa', 'finance/chart-of-accounts.html', 'chart-of-accounts', 'Chart of Accounts (COA)', 'دليل الحسابات الشجري', 'nav_chart_of_accounts'),
    ('journal_entries_s_acc_journal', 'finance/journal-entries.html', 'journal-entries', 'Journal Entries & Vouchers', 'قيود اليومية وسندات الصرف', 'nav_journal_entries'),
    ('treasury_cheques_s_acc_treasury', 'finance/treasury-cheques.html', 'treasury-cheques', 'Treasury & Cheques Portfolio', 'الخزينة ومحفظة الشيكات', 'nav_treasury_cheques'),
    ('daily_attendance_board_s_hr_board', 'hr/daily-attendance-board.html', 'daily-attendance-board', 'Daily Attendance Board', 'لوحة الحضور والانصراف اليومية', 'nav_attendance_board'),
    ('my_attendance_mobile_s_hr_my_attendance', 'hr/my-attendance-mobile.html', 'my-attendance-mobile', 'My Attendance Mobile Portal', 'سجل حضوري الذكي (موبايل)', 'nav_my_attendance'),
    ('security_permission_matrix_s_sec_matrix', 'security/security-permission-matrix.html', 'security-permission-matrix', 'Security Permission Matrix', 'مصفوفة صلاحيات المستخدمين', 'nav_security_permissions'),
    ('field_level_rules_masking_s_sec_fieldrules', 'security/field-level-rules.html', 'field-level-rules', 'Field-Level Rules & Masking', 'قواعد حجب وتشفير الحقول', 'nav_field_rules')
]

def generate_standard_sidebar(active_screen_id):
    def link_class(screen_id):
        if screen_id == active_screen_id:
            return 'flex items-center gap-3 px-3 py-2 rounded-lg transition-all bg-gradient-to-r from-secondary/20 to-primary-container/10 text-secondary border-l-2 border-secondary font-semibold shadow-[inset_0_1px_0_rgba(255,255,255,0.15)]'
        return 'flex items-center gap-3 px-3 py-2 rounded-lg font-body-sm text-body-sm text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-all'

    def aria_attr(screen_id):
        return ' aria-current="page"' if screen_id == active_screen_id else ''

    return f'''<aside class="fixed left-0 top-0 h-full w-[264px] bg-[#00142a]/95 backdrop-blur-2xl z-50 flex flex-col justify-between border-r border-white/10 shadow-[0_20px_50px_rgba(2,10,30,0.45)]">
  <div class="flex flex-col h-full overflow-hidden">
    <div class="h-[72px] px-space-lg flex items-center justify-between border-b border-white/10">
      <a href="../analytics/executive-dashboard.html" class="flex items-center group py-2">
        <img src="../assets/images/wise-logo.png" alt="Wise Distribution Logo" class="h-9 w-auto max-w-[170px] object-contain drop-shadow-[0_2px_10px_rgba(118,209,255,0.25)] group-hover:brightness-110 transition-all"/>
      </a>
      <a href="../index.html" class="text-on-surface-variant hover:text-secondary p-1.5 rounded-lg transition-colors" title="Showcase Portal">
        <span class="material-symbols-outlined text-[18px]">apps</span>
      </a>
    </div>

    <div class="flex-1 overflow-y-auto px-space-sm py-space-md space-y-space-md">
      <nav class="space-y-1">
        <!-- Analytics -->
        <div class="px-space-sm pt-2 pb-1 font-label-sm text-[11px] uppercase tracking-wider text-outline font-semibold" data-i18n="nav_analytics">Analytics</div>
        <a{aria_attr('executive-dashboard')} class="{link_class('executive-dashboard')}" data-path="executive-dashboard" href="../analytics/executive-dashboard.html">
          <span class="material-symbols-outlined text-[18px]">monitoring</span>
          <span data-i18n="nav_executive_dashboard">Executive Dashboard</span>
        </a>
        <a{aria_attr('reports-center')} class="{link_class('reports-center')}" data-path="reports-center" href="../analytics/reports-center.html">
          <span class="material-symbols-outlined text-[18px]">summarize</span>
          <span data-i18n="nav_reports_center">Reports Center</span>
        </a>

        <!-- Operations -->
        <div class="px-space-sm pt-4 pb-1 font-label-sm text-[11px] uppercase tracking-wider text-outline font-semibold" data-i18n="nav_operations">Operations &amp; Logistics</div>
        <a{aria_attr('products-catalog')} class="{link_class('products-catalog')}" data-path="products-catalog" href="../operations/products-catalog.html">
          <span class="material-symbols-outlined text-[18px]">category</span>
          <span data-i18n="nav_product_catalog">Product Catalog &amp; Prices</span>
        </a>
        <a{aria_attr('stock-availability')} class="{link_class('stock-availability')}" data-path="stock-availability" href="../operations/stock-availability.html">
          <span class="material-symbols-outlined text-[18px]">warehouse</span>
          <span data-i18n="nav_inventory_stock">Stock on Hand &amp; Availability</span>
        </a>
        <a{aria_attr('goods-receipts-grn')} class="{link_class('goods-receipts-grn')}" data-path="goods-receipts-grn" href="../operations/goods-receipts-grn.html">
          <span class="material-symbols-outlined text-[18px]">receipt_long</span>
          <span data-i18n="nav_grn_receipts">Goods Receipts (GRN)</span>
        </a>
        <a{aria_attr('inter-warehouse-transfers')} class="{link_class('inter-warehouse-transfers')}" data-path="inter-warehouse-transfers" href="../operations/inter-warehouse-transfers.html">
          <span class="material-symbols-outlined text-[18px]">move_up</span>
          <span data-i18n="nav_transfers">Inter-Warehouse Transfers</span>
        </a>
        <a{aria_attr('barcode-shelf-labels')} class="{link_class('barcode-shelf-labels')}" data-path="barcode-shelf-labels" href="../operations/barcode-shelf-labels.html">
          <span class="material-symbols-outlined text-[18px]">barcode_scanner</span>
          <span data-i18n="nav_barcode_labels">Barcode &amp; Shelf Labels</span>
        </a>

        <!-- Sales & CRM -->
        <div class="px-space-sm pt-4 pb-1 font-label-sm text-[11px] uppercase tracking-wider text-outline font-semibold" data-i18n="nav_sales">Sales &amp; CRM</div>
        <a{aria_attr('sales-pipeline-kanban')} class="{link_class('sales-pipeline-kanban')}" data-path="sales-pipeline-kanban" href="../sales/sales-pipeline-kanban.html">
          <span class="material-symbols-outlined text-[18px]">view_kanban</span>
          <span data-i18n="nav_pipeline_kanban">Pipeline &amp; Kanban</span>
        </a>
        <a{aria_attr('sales-quotation')} class="{link_class('sales-quotation')}" data-path="sales-quotation" href="../sales/sales-quotation.html">
          <span class="material-symbols-outlined text-[18px]">request_quote</span>
          <span data-i18n="nav_quotations">Sales Quotations</span>
        </a>
        <a{aria_attr('customer-360')} class="{link_class('customer-360')}" data-path="customer-360" href="../sales/customer-360.html">
          <span class="material-symbols-outlined text-[18px]">contacts</span>
          <span data-i18n="nav_customer_360">Customer 360</span>
        </a>

        <!-- Finance -->
        <div class="px-space-sm pt-4 pb-1 font-label-sm text-[11px] uppercase tracking-wider text-outline font-semibold" data-i18n="nav_finance">Finance &amp; Accounting</div>
        <a{aria_attr('chart-of-accounts')} class="{link_class('chart-of-accounts')}" data-path="chart-of-accounts" href="../finance/chart-of-accounts.html">
          <span class="material-symbols-outlined text-[18px]">table_chart</span>
          <span data-i18n="nav_chart_of_accounts">Chart of Accounts</span>
        </a>
        <a{aria_attr('journal-entries')} class="{link_class('journal-entries')}" data-path="journal-entries" href="../finance/journal-entries.html">
          <span class="material-symbols-outlined text-[18px]">menu_book</span>
          <span data-i18n="nav_journal_entries">Journal Entries</span>
        </a>
        <a{aria_attr('treasury-cheques')} class="{link_class('treasury-cheques')}" data-path="treasury-cheques" href="../finance/treasury-cheques.html">
          <span class="material-symbols-outlined text-[18px]">savings</span>
          <span data-i18n="nav_treasury_cheques">Treasury &amp; Cheques</span>
        </a>

        <!-- People -->
        <div class="px-space-sm pt-4 pb-1 font-label-sm text-[11px] uppercase tracking-wider text-outline font-semibold" data-i18n="nav_people">People &amp; HR</div>
        <a{aria_attr('daily-attendance-board')} class="{link_class('daily-attendance-board')}" data-path="daily-attendance-board" href="../hr/daily-attendance-board.html">
          <span class="material-symbols-outlined text-[18px]">how_to_reg</span>
          <span data-i18n="nav_attendance_board">HR Attendance Board</span>
        </a>
        <a{aria_attr('my-attendance-mobile')} class="{link_class('my-attendance-mobile')}" data-path="my-attendance-mobile" href="../hr/my-attendance-mobile.html">
          <span class="material-symbols-outlined text-[18px]">smartphone</span>
          <span data-i18n="nav_my_attendance">My Attendance (Mobile)</span>
        </a>

        <!-- Security -->
        <div class="px-space-sm pt-4 pb-1 font-label-sm text-[11px] uppercase tracking-wider text-outline font-semibold" data-i18n="nav_administration">Administration &amp; Security</div>
        <a{aria_attr('security-permission-matrix')} class="{link_class('security-permission-matrix')}" data-path="security-permission-matrix" href="../security/security-permission-matrix.html">
          <span class="material-symbols-outlined text-[18px]">security</span>
          <span data-i18n="nav_security_permissions">Security Permissions</span>
        </a>
        <a{aria_attr('field-level-rules')} class="{link_class('field-level-rules')}" data-path="field-level-rules" href="../security/field-level-rules.html">
          <span class="material-symbols-outlined text-[18px]">vpn_key</span>
          <span data-i18n="nav_field_rules">Field Rules &amp; Masking</span>
        </a>
      </nav>
    </div>

    <!-- Bottom Status Card -->
    <div class="p-space-md border-t border-white/10 bg-surface-container-low/70 backdrop-blur-md flex flex-col gap-space-xs">
      <div class="flex items-center justify-between">
        <span class="font-label-sm text-[12px] text-on-surface-variant flex items-center gap-1.5">
          <span class="material-symbols-outlined text-[14px] text-secondary">hub</span>
          <span data-i18n="cairo_central">Cairo Central Terminal</span>
        </span>
        <span class="flex h-2 w-2 relative">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
        </span>
      </div>
      <div class="flex items-center justify-between text-on-surface-variant">
        <span class="font-label-sm text-[11px] text-secondary-fixed" data-i18n="live_cloud_sync">Live Cloud Sync Active</span>
        <a href="../index.html" class="material-symbols-outlined text-[16px] text-outline hover:text-secondary cursor-pointer" title="Back to Portal Hub">home</a>
      </div>
    </div>
  </div>
</aside>'''

def generate_standard_header(title_en, title_ar, i18n_key):
    return f'''<header class="fixed top-0 left-[264px] right-0 h-[72px] z-40 bg-[#00142a]/90 backdrop-blur-xl border-b border-white/10 shadow-[0_20px_50px_rgba(2,10,30,0.45)] px-space-lg flex items-center justify-between gap-space-md">
  <!-- Breadcrumb -->
  <div class="flex items-center gap-2 font-label-md text-label-md text-on-surface-variant">
    <a href="../index.html" class="flex items-center text-secondary hover:text-on-surface transition-colors" title="Demo Home">
      <span class="material-symbols-outlined text-[18px]">home</span>
    </a>
    <span class="text-outline">/</span>
    <span class="text-outline hover:text-on-surface cursor-pointer" data-i18n="brand_name">Wise ERP</span>
    <span class="text-outline">/</span>
    <span class="text-on-surface font-semibold" data-i18n="{i18n_key}">{title_en}</span>
  </div>

  <!-- Search Input with Command Palette Trigger (Ctrl+K) -->
  <div class="flex-1 max-w-xl mx-space-md">
    <div class="relative flex items-center w-full header-search-wrap cursor-pointer" data-action="open-cmd">
      <span class="material-symbols-outlined absolute left-3 text-outline text-[20px]">search</span>
      <input class="w-full pl-10 pr-12 py-2 bg-[#04122b]/80 border border-white/15 rounded-lg text-on-surface placeholder:text-outline font-body-sm text-body-sm focus:outline-none focus:border-secondary transition-all cursor-pointer" placeholder="Search customers, products, documents, employees, deals (Ctrl+K)..." data-i18n-placeholder="search_placeholder" readonly type="text"/>
      <span class="absolute right-3 px-1.5 py-0.5 rounded bg-surface-container-high border border-white/10 font-label-sm text-label-sm text-on-surface-variant">⌘K</span>
    </div>
  </div>

  <!-- Right Actions: Hub, Language, Date, Notif, Create, Profile -->
  <div class="flex items-center gap-space-sm">
    <!-- Hub Selector -->
    <div class="relative">
      <select class="appearance-none bg-surface-container-high/60 border border-white/15 text-on-surface font-body-sm text-body-sm rounded-lg pl-3 pr-8 py-1.5 hover:bg-surface-container-highest cursor-pointer focus:outline-none focus:border-secondary">
        <option>Cairo HQ &amp; Central Hub</option>
        <option>Alexandria Coastal Hub</option>
        <option>Giza Fulfillment</option>
        <option>Delta Mansoura</option>
      </select>
      <span class="material-symbols-outlined absolute right-2 top-2 pointer-events-none text-outline text-[18px]">expand_more</span>
    </div>

    <!-- Bilingual Switcher -->
    <div class="flex items-center border border-white/15 rounded-lg p-0.5 bg-surface-container-high/40">
      <button data-lang-btn="en" class="px-2 py-0.5 rounded font-label-sm text-label-sm font-semibold bg-secondary-container text-on-secondary-container transition-all">EN</button>
      <button data-lang-btn="ar" class="px-2 py-0.5 rounded font-label-sm text-label-sm text-on-surface-variant hover:text-on-surface transition-all">ع</button>
    </div>

    <!-- Date Pill -->
    <div class="hidden xl:flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-white/15 bg-surface-container-high/40 font-body-sm text-body-sm text-on-surface-variant">
      <span class="material-symbols-outlined text-[16px] text-secondary">calendar_today</span>
      <span>Q4 2024 · Active Fiscal</span>
    </div>

    <!-- Notifications Bell -->
    <div class="relative">
      <button onclick="WiseERP.showToast({{ title: 'System Notifications', message: '5 operational alerts: 2 Low stock warnings, 1 Pending GRN voucher, 2 Shift approvals.', type: 'info' }})" class="p-2 rounded-lg border border-white/15 text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high transition-colors" title="Notifications">
        <span class="material-symbols-outlined text-[20px]">notifications</span>
      </button>
      <span class="notif-badge absolute -top-1 -right-1 px-1.5 py-0.2 rounded-full font-label-sm text-[10px] bg-secondary text-on-secondary font-bold shadow-[0_0_10px_rgba(118,209,255,0.6)]">5</span>
    </div>

    <!-- Quick Action / Create Button -->
    <a href="../sales/sales-quotation.html" class="flex items-center gap-1 px-3 py-1.5 rounded-lg font-body-sm text-body-sm font-semibold text-white bg-gradient-to-r from-secondary via-primary-container to-inverse-primary border border-white/30 shadow-[0_8px_24px_rgba(30,155,232,0.4)] hover:brightness-110 active:scale-95 transition-all">
      <span class="material-symbols-outlined text-[18px]">add</span>
      <span data-i18n="create_new">Create</span>
    </a>

    <div class="h-6 w-px bg-white/15 mx-1"></div>

    <!-- User Profile with Logout -->
    <a href="../auth/corporate-sso-login.html" title="Sign Out to SSO Login" class="flex items-center gap-3 pl-1 group hover:opacity-90 transition-opacity">
      <div class="flex flex-col text-right">
        <div class="flex items-center gap-1.5 justify-end">
          <span class="font-title-md text-title-md font-semibold text-on-surface group-hover:text-secondary transition-colors">Tarek El-Sayed</span>
          <span class="px-1.5 py-0.5 rounded-full font-label-sm text-[10px] font-bold bg-primary-container/20 text-secondary border border-secondary/30">Super Admin</span>
        </div>
        <span class="font-label-sm text-label-sm text-outline">Scope: All Hubs</span>
      </div>
      <img alt="Profile" class="w-8 h-8 rounded-full object-cover border border-secondary/40 shadow-[0_0_12px_rgba(91,203,255,0.2)]" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCultRCtgMRciVnK51-F0eUsLbvHS18gsIaQOxtHuKNKgGK7VdoAcDl4WgDbSh4XJ91VDiO50qXeDlh2vOYWYtqIlueYzfKqwUrqKJTHj0hymeNiiU-85wfsCNq8hfjNvNmvg1bEXYoxNnei7URQsxx59IdhDLKU2LngBC4FB7aOhLbBQMr216iGCzBul8s67Wl_IOkppRPIUtFFNEIsNY2a6XrqPz5ia7nCatKUCw"/>
    </a>
  </div>
</header>'''

def process_file(source_folder, dest_rel_path, screen_id, title_en, title_ar, i18n_key):
    src_path = os.path.join('_archive', source_folder, 'code.html')
    if not os.path.exists(src_path):
        print(f"Skipping {src_path}, file not found")
        return

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Head injection
    asset_injection = '''
  <link rel="icon" type="image/png" href="../assets/images/favicon.png"/>
  <link rel="shortcut icon" href="../assets/images/favicon.ico"/>
  <link rel="stylesheet" href="../assets/css/design-system.css"/>
  <script src="../assets/js/translations.js"></script>
  <script src="../assets/js/i18n.js"></script>
  <script src="../assets/js/nav-shell.js"></script>
'''

    # Ensure stylesheet and scripts are injected right before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{asset_injection}</head>')

    # For Corporate SSO Login
    if screen_id == 'corporate-sso-login':
        # Replace template placeholders
        content = content.replace('{{DATA:SCREEN:SCREEN_2}}', 'two-factor-authentication.html')
        content = content.replace('action="#"', 'action="two-factor-authentication.html"')
        content = re.sub(r'<form\b([^>]*)>', r'<form\1 onsubmit="event.preventDefault(); window.location.href=\'two-factor-authentication.html\';">', content)
        # Update SSO buttons
        content = content.replace('data-path="multi-factor-authentication" href="#"', 'href="two-factor-authentication.html"')
        content = content.replace('data-path="corporate-sso-login" href="#"', 'href="corporate-sso-login.html"')
        # Replace header brand with new logo
        content = re.sub(
            r'<div class="flex items-center gap-space-md">\s*<div class="w-10 h-10[^>]*>.*?</div>\s*<div class="flex flex-col">.*?</div>\s*</div>',
            '<a href="../index.html" class="flex items-center gap-3"><img src="../assets/images/wise-logo.png" alt="Wise Distribution" class="h-9 w-auto object-contain"/></a>',
            content,
            flags=re.DOTALL
        )
        # Replace language toggle button in header
        content = re.sub(
            r'<button[^>]*>\s*<span[^>]*>translate</span>\s*<span[^>]*>العربية</span>.*?EN</span>\s*</button>',
            '<div class="flex items-center border border-white/15 rounded-lg p-0.5 bg-surface-container-high/40"><button data-lang-btn="en" class="px-2 py-0.5 rounded font-label-sm text-label-sm font-semibold bg-secondary-container text-on-secondary-container">EN</button><button data-lang-btn="ar" class="px-2 py-0.5 rounded font-label-sm text-label-sm text-on-surface-variant hover:text-on-surface">ع</button></div>',
            content,
            flags=re.DOTALL
        )

    # For Two Factor Authentication
    elif screen_id == 'two-factor-authentication':
        content = content.replace('{{DATA:SCREEN:SCREEN_38}}', '../analytics/executive-dashboard.html')
        content = content.replace('data-path="corporate-sso-login" href="#"', 'href="corporate-sso-login.html"')
        content = content.replace('data-path="multi-factor-authentication" href="#"', 'href="two-factor-authentication.html"')
        # Replace header brand with new logo
        content = re.sub(
            r'<div class="flex items-center gap-space-md">\s*<div class="w-10 h-10[^>]*>.*?</div>\s*<div class="flex flex-col">.*?</div>\s*</div>',
            '<a href="../index.html" class="flex items-center gap-3"><img src="../assets/images/wise-logo.png" alt="Wise Distribution" class="h-9 w-auto object-contain"/></a>',
            content,
            flags=re.DOTALL
        )
        # Make Verify button route to executive dashboard
        content = re.sub(
            r'<button([^>]*)>\s*(?:<span[^>]*>verified_user</span>)?\s*(?:Verify &amp; Establish Session|Verify & Establish Session|Verify Identity|تحقق من الهوية).*?</button>',
            r'<button\1 onclick="WiseERP.showToast({ title: \'Session Verified\', message: \'Biometric MFA confirmed. Redirecting to Executive Command Console...\', type: \'success\' }); setTimeout(() => window.location.href=\'../analytics/executive-dashboard.html\', 1000);"><span class="material-symbols-outlined text-[18px]">verified_user</span><span>Verify &amp; Establish Session</span></button>',
            content,
            flags=re.DOTALL
        )
        content = re.sub(
            r'<button[^>]*>\s*<span[^>]*>translate</span>\s*<span[^>]*>العربية</span>.*?EN</span>\s*</button>',
            '<div class="flex items-center border border-white/15 rounded-lg p-0.5 bg-surface-container-high/40"><button data-lang-btn="en" class="px-2 py-0.5 rounded font-label-sm text-label-sm font-semibold bg-secondary-container text-on-secondary-container">EN</button><button data-lang-btn="ar" class="px-2 py-0.5 rounded font-label-sm text-label-sm text-on-surface-variant hover:text-on-surface">ع</button></div>',
            content,
            flags=re.DOTALL
        )

    # For My Attendance Mobile
    elif screen_id == 'my-attendance-mobile':
        # Replace header brand with new logo
        content = re.sub(
            r'<div class="flex items-center gap-space-sm min-w-0">\s*<div[^>]*hub.*?</div>\s*<div class="flex flex-col min-w-0">.*?</div>\s*</div>',
            '<a href="../index.html" class="flex items-center gap-2"><img src="../assets/images/wise-logo.png" alt="Wise Distribution" class="h-7 w-auto object-contain"/></a>',
            content,
            flags=re.DOTALL
        )
        # Replace language button
        content = re.sub(
            r'<button[^>]*aria-label="Switch Language"[^>]*>.*?</button>',
            '<div class="flex items-center border border-white/15 rounded-full p-0.5 bg-surface-container-high/60"><button data-lang-btn="en" class="px-2 py-0.5 rounded-full font-label-sm text-label-sm font-semibold bg-secondary-container text-on-secondary-container">EN</button><button data-lang-btn="ar" class="px-2 py-0.5 rounded-full font-label-sm text-label-sm text-on-surface-variant hover:text-on-surface">ع</button></div>',
            content,
            flags=re.DOTALL
        )
        # Add top banner linking to desktop attendance board
        mobile_banner = '''
        <div class="px-margin-mobile pt-3 pb-1">
          <a href="../hr/daily-attendance-board.html" class="flex items-center justify-between p-2.5 rounded-xl bg-gradient-to-r from-secondary/15 to-primary-container/20 border border-secondary/30 text-secondary hover:brightness-110 transition-all text-xs font-semibold">
            <div class="flex items-center gap-2">
              <span class="material-symbols-outlined text-[18px]">desktop_windows</span>
              <span>Switch to HR Enterprise Daily Board</span>
            </div>
            <span class="material-symbols-outlined text-[16px]">arrow_forward</span>
          </a>
        </div>
        '''
        content = content.replace('<main class="flex flex-col relative w-full pt-16 pb-28 px-margin-mobile bg-surface z-10 min-h-screen">', f'<main class="flex flex-col relative w-full pt-16 pb-28 px-margin-mobile bg-surface z-10 min-h-screen">{mobile_banner}')

    # Standard Internal Dashboard Screens (16 screens)
    else:
        # Standardize sidebar
        new_sidebar = generate_standard_sidebar(screen_id)
        content = re.sub(r'<aside\b[^>]*>.*?</aside>', new_sidebar, content, flags=re.DOTALL)

        # Standardize top header
        new_header = generate_standard_header(title_en, title_ar, i18n_key)
        content = re.sub(r'<header\b[^>]*>.*?</header>', new_header, content, flags=re.DOTALL)

    # Cross-screen contextual business logic links
    if screen_id == 'sales-quotation':
        content = content.replace('{{DATA:SCREEN:SCREEN_32}}', 'customer-360.html')
        content = content.replace('href="#"', 'href="javascript:void(0)"')
        # Link to customer 360 & pipeline
        content = content.replace('View Customer History', '<a href="customer-360.html" class="text-secondary hover:underline">View Customer History</a>')
        content = content.replace('Convert to Sales Order', '<a href="sales-pipeline-kanban.html" class="contents">Convert to Sales Order</a>')

    elif screen_id == 'customer-360':
        content = content.replace('+ New Sales Order', '<a href="sales-quotation.html" class="contents">+ New Sales Quotation</a>')
        content = content.replace('View Full Ledger', '<a href="../finance/journal-entries.html" class="contents">View Full Ledger</a>')

    elif screen_id == 'goods-receipts-grn':
        content = content.replace('Scan Pallet / Barcode', '<a href="barcode-shelf-labels.html" class="contents">Scan Pallet / Barcode</a>')
        content = content.replace('+ New Inbound Receipt', '<a href="stock-availability.html" class="contents">+ New Inbound Receipt</a>')

    elif screen_id == 'stock-availability':
        content = content.replace('Initiate Transfer', '<a href="inter-warehouse-transfers.html" class="contents">Initiate Transfer</a>')
        content = content.replace('Print Barcode Labels', '<a href="barcode-shelf-labels.html" class="contents">Print Barcode Labels</a>')
        content = content.replace('Record New GRN', '<a href="goods-receipts-grn.html" class="contents">Record New GRN</a>')

    elif screen_id == 'security-permission-matrix':
        content = content.replace('Manage Field Masking Rules', '<a href="field-level-rules.html" class="contents">Manage Field Masking Rules</a>')

    elif screen_id == 'field-level-rules':
        content = content.replace('Back to Permission Matrix', '<a href="security-permission-matrix.html" class="contents">Back to Permission Matrix</a>')

    elif screen_id == 'daily-attendance-board':
        content = content.replace('Mobile Clock-in Simulator', '<a href="my-attendance-mobile.html" class="contents">Mobile Clock-in Simulator</a>')

    os.makedirs(os.path.dirname(dest_rel_path), exist_ok=True)
    with open(dest_rel_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Optimized & migrated: {dest_rel_path}")

def main():
    print("Starting Wise ERP screen optimization and migration...")
    for cfg in SCREEN_CONFIGS:
        process_file(*cfg)
    print("All 19 screens successfully migrated and optimized!")

if __name__ == '__main__':
    main()
