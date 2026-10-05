# Agentic QA Workflow Framework 🧪🤖

> **Framework Penjaminan Mutu Berbasis AI-Augmented Quality Engineering (Human-in-the-Loop)**  
> Dirancang agar setiap kali membangun fitur perangkat lunak (*software build*), AI Agent atau Software Engineer wajib membaca **PRD versi QA** sebelum mulai coding, lalu mengeksekusi siklus penjaminan mutu 5 tahap.

---

## 📌 Mengapa Framework Ini Diciptakan?

Pada era AI coding, membuat kode dan ratusan test case otomatis (seperti via BrowserStack Companion atau AI test generator) sangatlah cepat. Namun timbul risiko besar:
1. **False Sense of Security (Status Hijau Palsu)**: Robot Playwright sering memberi status `PASS` hanya karena elemen tombol berhasil diklik, padahal data di database belum tersimpan atau ada celah keamanan fatal (misal: password salah tetap redirect ke dasbor).
2. **AI Hallucination & Test Bloat**: Ratusan skenario dangkal terbuat, tetapi aturan bisnis krusial (seperti pengecualian PPN 11%, batasan pagu anggaran, isolasi multi-peran) terlewat.
3. **Kelelahan Uji Manual (QA Fatigue)**: Menguji manual 400+ skenario satu per satu menghabiskan waktu berminggu-minggu.

**Solusi:** Framework ini menggabungkan kecepatan otomasi AI (80%) dengan ketelitian validasi manusia (20% pada titik risiko tinggi) menggunakan classifier cerdas **Laya**.

---

## 🔄 Siklus 5 Tahap (The 5-Phase QA Loop)

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   0. QA-DRIVEN REQUIREMENT & PRD                       │
│  (Batasan Hak Akses, State Machine, Aturan PPN/Finansial, Kasus Negatif)│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  Phase 1: Exploration & Drafting (BrowserStack Companion / AI)         │
│  - Crawling journeys utama -> Ekstrak baseline DOM -> Draft Test Case  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  Phase 2: Automated Regression (Playwright CLI / Playwright MCP)       │
│  - Jalankan ratusan skenario -> Tangkap logs/traces -> evidence.json   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  Phase 3: Agent Domain & Logic Audit (Agent Skill)                     │
│  - Audit kepatuhan PPN (PP 49/2022), mitigasi bypass auth & sanitasi   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  Phase 4: Post-Test ML Classification (Laya Classifier)                │
│  - Klasifikasi bukti: integration_success, auth_issue, state_desync    │
│  - Triage otomatis: WAJIB MANUAL 🔴 | SAMPLING 🟡 | AUTO PASS 🟢        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  Phase 5: Human-in-the-Loop Validation (QA Engineer)                   │
│  - Uji headed pada 20-30 TC kritis -> Bug Report standar CWE/OWASP     │
└────────────────────────────────────────────────────────────────────────┘
```

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
