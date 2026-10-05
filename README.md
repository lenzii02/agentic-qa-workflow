# Agentic QA Workflow Framework 🧪🤖

> **Precision AI-Augmented QA Stack (Human-in-the-Loop)**  
> Framework penjaminan mutu software modern berbasis integrasi 5 tools utama:  
> **Extension Test Companion (BrowserStack AI) ➔ Playwright MCP (Status & Actual) ➔ Agent Skill (Coverage, Cross-Role, Rumus/Pajak, Bug Report) ➔ Laya Decision Model ➔ Google Sheets MCP**

---

## 🛠️ The 5-Pillar Tooling Stack

Framework ini bekerja dengan 5 komponen terintegrasi yang saling melengkapi:

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             0. QA-DRIVEN PRD                                     │
│          (Matriks Role Boundary, State Transitions, Aturan Rumus Pajak/Finansial)│
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ 1. Extension Test Companion (Otak BrowserStack)                                  │
│    - Exploratory crawling cerdas langsung dari peramban                           │
│    - Generate draf Test Cases (CSV) otomatis berbasis AI BrowserStack            │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ 2. Playwright MCP (Status & Actual Result Collector)                             │
│    - Menjalankan otomasi browser (headless/headed) via protokol MCP               │
│    - Eksekusi regresi skala besar, tangkap Status (Pass/Fail) & Actual Evidence  │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ 3. Agent Skill (Coverage, Cross-Testing, Rumus/Pajak, Bug Report)                │
│    - Analisis Coverage Gap (skenario kritis yang belum ter-cover)                │
│    - Eksekusi Cross-Role Testing (interaksi bertingkat antar-akun/peran)          │
│    - Verifikasi Rumus Bisnis & PPN (BKP 11% vs Non-BKP 0% PP 49/2022)            │
│    - Generate Bug Report terstandarisasi OWASP / CWE                             │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ 4. Laya Decision Model (Post-Test ML Triage Engine)                              │
│    - Evaluasi evidence.json: integration_success, auth_issue, state_desync       │
│    - Triage otomatis: WAJIB QA MANUAL 🔴 | DISARANKAN SAMPLING 🟡 | AUTO PASS 🟢 │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│ 5. Google Sheets MCP (Automated Master Sync)                                     │
│    - Sync hasil akhir evaluasi langsung ke Google Sheets master QA               │
│    - Update status test case, PIC tester, evidence link, & log bug otomatis      │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Rincian Peran Tiap Tool dalam Workflow

### 1. Extension Test Companion (Otak BrowserStack)
- **Fungsi:** Menggantikan pencatatan skenario manual yang lambat.
- **Cara Kerja:** Terpasang di browser, merekam interaksi pengguna, menganalisis struktur DOM, dan secara otomatis menyusun draf awal test case ke format CSV lengkap dengan precondition, langkah, dan ekspektasi.

### 2. Playwright MCP (Status & Actual Evidence)
- **Fungsi:** Mesin eksekusi otomatisasi browser handal via Model Context Protocol.
- **Cara Kerja:** Menerima aksi pengujian, mengontrol peramban web, menangkap network payload, screenshot kegagalan, dan menghasilkan `Status` (Passed/Failed) beserta `Actual Result` yang objektif.

### 3. Agent Skill (Coverage, Cross-Testing, Rumus, & Bug Reporting)
- **Coverage Analysis:** Mendeteksi edge cases dan boundary yang belum tercakup oleh crawler awal.
- **Cross-Testing Orchestration:** Menguji alur berantai multi-peran (misal: Aktor A submit produk ➔ Aktor B beli di katalog ➔ Aktor C approve pesanan).
- **Audit Rumus & Perpajakan:** Memvalidasi kalkulasi matematika kompleks:
  - Diskon promo & penyesuaian harga negosiasi.
  - Validasi PPN kondisional: Barang Kena Pajak (11%) vs Bebas PPN (0% sesuai PP 49/2022 untuk buku pelajaran).
  - Pembulatan desimal nilai transaksi belanja instansi.
- **Standardized Bug Report:** Menerbitkan laporan defect berstandar industri dengan pemetaan CWE / OWASP.

### 4. Laya Decision Model (Post-Test ML Triage Engine)
- **Fungsi:** Filter cerdas untuk menghilangkan fenomena *false-pass* pada robot otomasi.
- **Cara Kerja:** Menganalisis `evidence.json` dari Playwright dan Agent. Mengelompokkan hasil ke:
  - 🔴 **WAJIB QA MANUAL**: Test berstatus Fail, celah keamanan (auth bypass / session leak), atau evidence tidak lengkap.
  - 🟡 **DISARANKAN SAMPLING**: Transisi status antar-peran, kalkulasi angka/uang, dan ekspor file.
  - 🟢 **AUTO PASS CUKUP**: UI layout dan navigasi dasar yang lolos tanpa anomali.

### 5. Google Sheets MCP (Master QA Sync)
- **Fungsi:** Integrasi pelaporan tanpa copy-paste manual.
- **Cara Kerja:** Melalui tool `google-sheets-mcp`, hasil klasifikasi Laya dan status validasi QA langsung di-push ke Google Spreadsheet master project secara real-time.

---

## 📂 Struktur Repositori

```text
agentic-qa-workflow/
├── SKILL.md                        # Definisi skill untuk Hermes, OpenCode, Claude Code
├── README.md                       # Dokumentasi utama framework
├── .agent/
│   └── agent.md                    # Konfigurasi agen untuk Antigravity, OpenCode, Cursor
├── prd/
│   ├── QA_DRIVEN_PRD_TEMPLATE.md   # Template PRD wajib sebelum build fitur
│   ├── STATE_TRANSITION_MATRIX.md  # Template state machine multi-aktor
│   └── TAX_AND_BUSINESS_RULES.md   # Template kalkulasi PPN & aturan bisnis
├── workflows/
│   ├── 01-exploration-and-drafting.md
│   ├── 02-playwright-regression.md
│   ├── 03-agent-domain-auditing.md
│   ├── 04-laya-ml-classification.md
│   └── 05-human-in-the-loop-qa.md
├── templates/
│   ├── test-cases-template.csv     # Skema CSV test cases terstandarisasi
│   ├── bug-report-template.md      # Template laporan cacat (OWASP / CWE)
│   ├── evidence-schema.json        # Skema JSON evidence untuk model ML
│   └── release-quality-gate.md     # Checklist kriteria rilis ke production
├── scripts/
│   ├── build-evidence.mjs          # Script ekstraksi Playwright -> evidence.json
│   └── laya-triage-runner.py       # Script triage Laya (JSON -> CSV/MD matrix)
└── examples/
    └── eprocurement-tisera-sample.md # Studi kasus nyata implementasi Tisera
```

---

## 🚀 Panduan Penggunaan Sebelum Build

Setiap kali hendak membuat fitur baru atau merefaktor sistem:

1. **Buka dan Salin Template PRD:**
   Gunakan file `prd/QA_DRIVEN_PRD_TEMPLATE.md`. Isi peran yang terlibat, batasan akses (siapa yang diblokir), aturan kalkulasi angka/uang, dan skenario kegagalan.
2. **Perintahkan AI Coding Agent:**
   Berikan instruksi:
   > *"Baca dokumen `prd/QA_DRIVEN_PRD_TEMPLATE.md` dan `SKILL.md` sebelum mengimplementasikan fitur ini. Pastikan seluruh acceptance criteria dan boundary test tervalidasi."*
3. **Eksekusi Regresi & Klasifikasi Laya:**
   ```bash
   # 1. Jalankan Playwright
   npx playwright test --reporter=list,json

   # 2. Bangun evidence terstruktur
   node scripts/build-evidence.mjs

   # 3. Jalankan klasifikasi triage Laya
   python scripts/laya-triage-runner.py --input evidence/evidence.json
   ```
4. **Validasi Manual Human-in-the-Loop:**
   Buka file `Laya_QA_Manual_Validation.csv`, filter daftar **WAJIB QA MANUAL**, dan verifikasi langsung di peramban.

---

## 📄 Lisensi & Kontributor
- **Author:** [lenzii02](https://github.com/lenzii02)
- **Lisensi:** MIT License
