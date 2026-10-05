---
name: agentic-qa-workflow
description: End-to-end AI-augmented QA workflow — from QA-driven PRD definition, Companion TC drafting, Playwright MCP regression, domain & tax audit, to Laya ML classification and human-in-the-loop validation.
version: 1.0.0
author: lenzii02
category: software-development
tags: [qa, testing, playwright, laya, agentic-qa, test-automation, prd, quality-engineering]
---

# Agentic QA Workflow Skill

Skill ini memandu AI Agent (Hermes, Claude Code, Antigravity, OpenCode, Cursor) untuk mengeksekusi siklus penjaminan mutu perangkat lunak end-to-end dengan pendekatan **Hybrid AI-Augmented Quality Engineering**.

Sebelum developer/agent menulis kode atau menjalankan build, agent **wajib membaca PRD & Requirement berbasis QA** yang tertera di repository ini.

---

## Prinsip Inti (Core Tenets)

1. **Shift-Left QA via QA-Driven PRD**:
   Kebutuhan software harus dirumuskan dari kacamata *testability*, batasan peran (role boundary), kalkulasi finansial (PPN/pajak), dan state transition sebelum implementasi dimulai.
2. **Zero Blind Faith on Green Tests**:
   Status `PASS` Playwright tidak menjamin ketiadaan bug logika atau celah keamanan (contoh: bypass password salah yang lolos karena sekadar redirect).
3. **Evidence-Driven Post-Test Classification**:
   Semua output otomatisasi harus diekstrak menjadi `evidence.json`, kemudian difilter oleh classifier cerdas (seperti **Laya**) untuk memisahkan hasil bersih dari potensi desinkronisasi data, kelemahan otorisasi, atau artifact ambigu.
4. **Human-in-the-Loop as Final Validator**:
   AI mengotomasi 80% beban repetitif (form filling, regression, evidence scraping, formatting); QA manual memvalidasi 20% area risiko tinggi (security, state transition, edge cases).

---

## Siklus 5 Tahap (The 5-Phase Loop)

```
[PRD / Requirements QA Version]
              │
              ▼
[Phase 1: Exploration & Drafting]  (BrowserStack Companion / AI Exploration)
              │
              ▼
[Phase 2: Playwright Regression]   (Playwright CLI / MCP + Evidence Builder)
              │
              ▼
[Phase 3: Domain & Logic Audit]    (Tax/PPN rules, Auth, State Transitions)
              │
              ▼
[Phase 4: Laya AI/ML Filtering]    (Laya Classifier: Triage Wajib vs Sampling vs Auto Pass)
              │
              ▼
[Phase 5: Human QA Validation]     (Targeted Manual QA, OWASP/CWE Bug Report, Sheets Sync)
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
