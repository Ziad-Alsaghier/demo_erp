# Wise ERP - Enterprise Distribution & Fleet Operating System (Demo Suite)

> **Design System:** Luminous Enterprise Fleet · Version 2024.4  
> **Standards Compliance:** Egyptian Accounting Standards (EAS) · ETA e-Invoice v2.1 Ready · SOC2 Type II · ISO 27001  
> **Localization:** 100% Arabic & English Bilingual · Dynamic Real-time RTL/LTR Engine

---

## 🚀 Quick Start & How to Run

1. Open `index.html` directly in any modern web browser (Chrome, Edge, Firefox, Safari).  
   *Alternatively, run a local web server:*
   ```bash
   # Python 3
   python -m http.server 8080
   # or Node.js npx serve
   npx serve .
   ```
2. Open `http://localhost:8080` to experience the **Showcase Portal & Gateway**.
3. Use the top-right language switcher (**English | العربية**) on any page to toggle instantaneously between English (LTR, Inter / Plus Jakarta Sans) and Arabic (RTL, Cairo Typography). Your language preference is automatically persisted across all screens via `localStorage`.
4. Press `Ctrl+K` (or `⌘K` on macOS) anywhere to launch the **Enterprise Command Palette** to jump to any screen or trigger quick actions.

---

## 📁 Optimized Project Architecture

```
stitch_wise_erp_design_system/
├── index.html                           # Main Demo Showcase & System Gateway
├── assets/
│   ├── css/
│   │   └── design-system.css            # Unified tokens, RTL overrides, Cairo fonts, toasts & palette
│   ├── js/
│   │   ├── translations.js              # Curated bilingual enterprise dictionary (EN & AR)
│   │   ├── i18n.js                      # Dynamic runtime translation & RTL/LTR engine
│   │   └── nav-shell.js                 # Unified navigation, active indicators, Ctrl+K, Toasts
│   ├── images/                          # High-res screen previews and system logos
│   └── DESIGN.md                        # Design tokens specification (colors, typography, spacing)
├── auth/
│   ├── corporate-sso-login.html         # Corporate SSO Login (Entry Gateway)
│   └── two-factor-authentication.html   # Biometric & Hardware MFA Verification
├── analytics/
│   ├── executive-dashboard.html         # Executive Command & Operational Metrics
│   └── reports-center.html              # Multi-hub BI & Operational Reports Center
├── operations/
│   ├── products-catalog.html            # Product Catalog & Multi-tier Price Lists
│   ├── stock-availability.html          # Stock on Hand & Real-time Availability
│   ├── goods-receipts-grn.html          # Goods Receipts Notes (GRN) & Inbound Inspection
│   ├── inter-warehouse-transfers.html   # Inter-Warehouse Fleet Custody Transfers
│   └── barcode-shelf-labels.html        # Barcode & Shelf Label Print Center
├── sales/
│   ├── sales-pipeline-kanban.html       # B2B Deals & Opportunity Kanban Board
│   ├── sales-quotation.html             # Multi-currency Sales Quotation Builder
│   └── customer-360.html                # Enterprise Customer 360 Dossier
├── finance/
│   ├── chart-of-accounts.html           # Hierarchical Chart of Accounts (COA) Tree
│   ├── journal-entries.html             # General Ledger & Multi-line Journal Vouchers
│   └── treasury-cheques.html            # Treasury, Cheque Portfolio & Cash Positions
├── hr/
│   ├── daily-attendance-board.html      # Workforce Attendance & Shift Radar
│   └── my-attendance-mobile.html        # Employee Mobile Self-Service Simulator
├── security/
│   ├── security-permission-matrix.html  # Role-Based Access Control (RBAC) Matrix
│   └── field-level-rules.html           # Field-Level Masking & Data Privacy Rules
├── _archive/                            # Preserved original raw Stitch UI screen folders
└── _scripts/                            # Maintenance and verification scripts
```

---

## 🌐 Dynamic Localization & Translation (Arabic & English)

- **Bidirectional Layout (RTL & LTR)**:
  - Switching to Arabic immediately mirrors the application layout: the fixed navigation sidebar smoothly moves from left to right, content padding adjusts from `pl-[264px]` to `pr-[264px]`, breadcrumb paths invert, and search inputs align with mirrored icons.
- **Enterprise Typography**:
  - English: `Plus Jakarta Sans` for headlines and `Inter` for metrics and tables.
  - Arabic: `Cairo` web font with balanced typographic weights.
- **Curated Translations**:
  - Standardized against official Egyptian logistics and financial terminology (e.g. *أذون استلام البضائع GRN*, *التحويلات بين المستودعات*, *دليل الحسابات*, *قيود اليومية المحاسبية*, *محفظة الشيكات*, *مصفوفة الصلاحيات والحماية*, *حجب وتشفير الحقول الحساسة*).

---

## 🔗 Business Workflow Linkages

The demo connects screens based on real enterprise business processes:

1. **Authentication Flow**:  
   `corporate-sso-login.html` ➡️ `two-factor-authentication.html` ➡️ `executive-dashboard.html`
2. **Inbound & Supply Chain Cycle**:  
   `goods-receipts-grn.html` ➡️ `stock-availability.html` ➡️ `inter-warehouse-transfers.html` ➡️ `barcode-shelf-labels.html`
3. **Commercial & Sales Pipeline**:  
   `sales-pipeline-kanban.html` ➡️ `sales-quotation.html` ➡️ `customer-360.html` ➡️ `journal-entries.html`
4. **General Ledger & Treasury Governance**:  
   `chart-of-accounts.html` ➡️ `journal-entries.html` ➡️ `treasury-cheques.html`
5. **Workforce Operations**:  
   `daily-attendance-board.html` 🔁 `my-attendance-mobile.html` (Desktop ↔ Mobile simulator toggle)
6. **Security & Data Governance**:  
   `security-permission-matrix.html` 🔁 `field-level-rules.html`

---

## ⚡ Enterprise Interactivity

- **Command Palette (`Ctrl+K` / `⌘K`)**: Quick launcher supporting instant screen filtering and quick action triggers.
- **Toast Notifications**: Realistic visual feedback when clicking "Export", "Save", "Approve Voucher", "Print Labels", or changing operating hubs.
- **Active Navigation States**: Every page automatically highlights its active item in the master sidebar.
- **Operating Hub Selector**: Allows switching between Cairo HQ, Alexandria, Giza, and Delta fulfillment hubs.
- **Currency Toggle**: Interactive switching between EGP and USD figures.
