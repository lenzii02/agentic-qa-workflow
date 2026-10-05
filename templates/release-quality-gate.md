# Release Quality Gate Checklist

Gunakan checklist ini sebelum menandatangani persetujuan rilis ke lingkungan Production:

---

## 1. Automation Execution Gate
- [ ] Rangkaian tes regresi Playwright selesai dijalankan 100%.
- [ ] Nol (0) tes berstatus *unhandled crash* atau *hung process*.
- [ ] Artifact JSON (`results.json`) dan bukti screenshot kegagalan tersimpan rapi.

## 2. Laya Post-Test ML Gate
- [ ] Ekstraksi `evidence.json` berhasil diproses oleh model Laya.
- [ ] Tidak ada temuan kategori `critical_blocker` yang belum terselesaikan.
- [ ] Tidak ada indikasi `authorization_issue` terbuka di lingkungan staging.

## 3. Human-in-the-Loop Manual QA Gate
- [ ] Seluruh item berkategori **WAJIB QA MANUAL** telah direproduksi langsung oleh QA.
- [ ] Uji sampling (10-20%) pada kalkulasi nominal uang, PPN, dan approval berantai dinyatakan valid.
- [ ] Seluruh defect P0 (Blocker) dan P1 (High) telah diperbaiki oleh tim developer dan lolos uji ulang (*re-test*).

## 4. Business & Regulatory Gate
- [ ] Perhitungan PPN (11% BKP vs 0% Bebas PPN sesuai regulasi) terverifikasi konsisten di antarmuka web, faktur PDF, dan database.
- [ ] Mekanisme proteksi sesi (logout, expired token, multi-role isolation) berfungsi optimal.

---

**Keputusan Rilis:**
- [ ] **GO (Siap Rilis)**: Semua kriteria di atas terpenuhi.
- [ ] **NO-GO (Tunda Rilis)**: Masih terdapat defect kritis yang belum tertangani.

*Tanda tangan QA Lead:* ___________________  
*Tanggal Evaluasi:* ___________________
