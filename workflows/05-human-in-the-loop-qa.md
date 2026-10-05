# Phase 5: Human-in-the-Loop QA Validation & Defect Lifecycle

## 1. Tujuan
Memaksimalkan efisiensi waktu QA Engineer dengan memfokuskan tenaga manusia hanya pada test case berisiko tinggi (kategori `WAJIB QA MANUAL`), investigasi akar masalah bug, serta pelaporan defect yang terstandarisasi.

---

## 2. Prosedur Uji Manual Terarah

1. **Buka Laporan Triage:**
   - Akses file `Laya_QA_Manual_Validation.csv` atau `laya-qa-manual-validation.md`.
   - Filter baris dengan kolom `Recommendation = "WAJIB QA MANUAL"`.
2. **Reproduksi di Browser Nyata (Headed Mode):**
   - Jalankan skenario secara manual di browser dengan DevTools (F12) terbuka.
   - Amati tab **Network** (status code dan payload JSON) serta tab **Console** (log JavaScript).
3. **Eksplorasi Skenario Edge-Case:**
   - Lakukan pengujian di luar jalur linear:
     - Mengklik tombol aksi berkali-kali secara cepat (double click / spam submit).
     - Menekan tombol Back peramban setelah logout atau setelah checkout.
     - Mengubah nominal parameter URL secara manual (IDOR test).

---

## 3. Standarisasi Pelaporan Defect (Bug Report)

Jika anomali terkonfirmasi sebagai cacat sistem (bug), buat laporan menggunakan `templates/bug-report-template.md`:
- Sertakan **CWE / OWASP Identifier** untuk isu keamanan.
- Tentukan **Severity** (Critical/Major/Minor) dan **Priority** (P0/P1/P2).
- Sertakan **Steps to Reproduce** yang presisi, **Expected Result**, **Actual Result**, serta **Tangkapan Layar Bukti**.

---

## 4. Sinkronisasi ke Spreadsheet / Pelacak Tugas

Perbarui status test case pada Google Sheets master tracking:
- Status `PASS`: Telah terverifikasi via otomasi atau lolos uji manual.
- Status `FAIL`: Bug terkonfirmasi dan tiket defect telah dibuat.
- Status `BLOCKED`: Terhalang bug blocker hulu (misal: gagal login sehingga fitur transaksi tidak dapat diuji).
