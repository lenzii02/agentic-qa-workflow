---
name: agentic-qa-workflow
description: End-to-end AI-augmented QA workflow — Extension Test Companion (BrowserStack AI), Playwright MCP (status & actual), Agent Skill (coverage, cross-testing, rumus & bug report), Laya Decision Model, and Google Sheets MCP.
version: 1.1.0
author: lenzii02
category: software-development
tags: [qa, testing, test-companion, browserstack, playwright-mcp, agent-skill, laya, gsheets-mcp]
---

# Agentic QA Workflow Skill

Skill ini memandu AI Agent (Hermes, Claude Code, Antigravity, OpenCode, Cursor) untuk mengeksekusi siklus penjaminan mutu software modern dengan integrasi 5 tools utama:
1. **Extension Test Companion (Otak BrowserStack)**: Eksplorasi UI & draf skenario otomatis.
2. **Playwright MCP**: Eksekutor peramban untuk menangkap `Status` (Pass/Fail) dan `Actual Evidence`.
3. **Agent Skill**: Audit cakupan test (coverage), pengujian silang multi-peran (cross-testing), verifikasi rumus/PPN, dan format bug report standar OWASP/CWE.
4. **Laya Decision Model**: Classifier AI/ML untuk membedakan false-pass dan menyeleksi test case yang wajib divalidasi manusia.
5. **Google Sheets MCP**: Sinkronisasi otomatis data pengujian ke Google Sheets master.

---

## Prinsip Inti (Core Tenets)

1. **Shift-Left QA via QA-Driven PRD**:
   Spesifikasi software wajib dirumuskan dari kacamata testability sebelum coding/build: role boundary matrix, transisi state machine, dan rumus bisnis finansial/PPN.
2. **Zero Blind Faith on Green Automation**:
   Status `PASS` Playwright tidak menjamin bebas bug. Perlu audit actual evidence, network payload, dan log anomali.
3. **Evidence-Driven Post-Test Triage via Laya**:
   Semua output otomatisasi diekstrak ke `evidence.json` lalu diproses oleh **Laya Decision Model** untuk memisahkan hasil bersih dari celah otorisasi, desync status, atau error tersembunyi.
4. **Human-in-the-Loop as Final Validator**:
   Otomasi menangani 80% beban repetitif; QA manual memverifikasi 20% area risiko tinggi hasil saringan Laya.
5. **Automated Master Reporting**:
   Hasil triage dan status bug langsung diunggah via Google Sheets MCP tanpa entri manual.

---

## Siklus 5 Tahap (The 5-Pillar Loop)

```
[QA-Driven PRD / Requirements Baseline]
                  │
                  ▼
[1. Extension Test Companion] ➔ Otak BrowserStack untuk crawling & draf CSV skenario awal
                  │
                  ▼
[2. Playwright MCP]           ➔ Eksekusi headless/headed, kumpulkan Status & Actual Result
                  │
                  ▼
[3. Agent Skill]              ➔ Audit Coverage, Cross-Role testing, Rumus Pajak/PPN, Bug Report
                  │
                  ▼
[4. Laya Decision Model]      ➔ ML Triage: WAJIB QA MANUAL 🔴 | SAMPLING 🟡 | AUTO PASS 🟢
                  │
                  ▼
[5. Google Sheets MCP]        ➔ Push hasil evaluasi & bug log langsung ke Master Spreadsheet
```

---

## Petunjuk Penggunaan untuk AI Coding Agent

Ketika user meminta: *"Build fitur X"* atau *"Test aplikasi Y"*:

1. **Langkah 1**: Baca `prd/QA_DRIVEN_PRD_TEMPLATE.md` dan pastikan spesifikasi fitur mencakup:
   - User roles & permission boundary.
   - Exact input validation rules.
   - Financial/tax calculation formulas.
   - Negative test scenarios & edge cases.
2. **Langkah 2**: Buat test suite Playwright mengikuti pola modular (`tests/<role>/<module>.spec.ts`).
3. **Langkah 3**: Eksekusi test suite dan ekstrak `evidence.json` via `scripts/build-evidence.mjs`.
4. **Langkah 4**: Jalankan classifier Laya (`scripts/laya-triage-runner.py`) untuk membagi test case ke dalam 3 tier:
   - 🔴 **WAJIB QA MANUAL**: Test berstatus Fail, boundary auth/security, atau evidence tidak lengkap.
   - 🟡 **DISARANKAN SAMPLING**: State approval multi-role, kalkulasi nominal uang/pajak, upload/export.
   - 🟢 **AUTO PASS CUKUP**: UI layout dan smoke test dasar yang sudah terbukti lolos.
5. **Langkah 5**: Laporkan ringkasan temuan ke user dengan format tabel prioritasi dan sediakan checklist eksekusi manual untuk QA.
