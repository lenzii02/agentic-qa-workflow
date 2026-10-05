# Phase 3: Domain & Business Logic Auditing (Agent Skill)

## 1. Tujuan
Memanfaatkan keahlian penalaran AI Agent untuk mengidentifikasi celah logika bisnis, kelemahan otorisasi, dan ketidaksesuaian regulasi yang luput dari skrip otomasi Playwright standar.

---

## 2. Area Audit Utama AI Agent

1. **Audit Perpajakan & Kalkulasi:**
   - Memeriksa apakah kalkulasi PPN (11%) atau PPh sudah sesuai dengan kategori barang (BKP vs Non-BKP) dan status vendor (PKP vs Non-PKP).
   - Memastikan bahwa diskon atau negosiasi harga menurunkan Dasar Pengenaan Pajak (DPP).
2. **Audit Boundary Otorisasi (Access Control):**
   - Menguji apakah token sesi atau storage state antar akun bocor.
   - Menguji apakah pengguna peran rendah dapat mengakses rute internal peran tinggi (misal: Buyer membuka `/admin` atau `/vendor`).
3. **Audit Konsistensi Antar Sesi (Multi-Role State):**
   - Memverifikasi konsistensi data dari hulu ke hilir:
     Contoh: Produk disubmit di sisi Penyedia -> Tampil di antarmuka Approver -> Berhasil dibeli oleh Pembeli.
4. **Audit Validasi Input & Sanitasi:**
   - Menguji respons sistem terhadap payload injection (XSS / SQLi sederhana) pada kolom pencarian dan form filter.

---

## 3. Output Tahap Audit

Agent menghasilkan catatan verifikasi awal dan rekomendasi skenario tambahan yang perlu dimasukkan ke dalam evidence sebelum diproses oleh classifier model ML.
