# Case Study: E-Procurement Tisera Implementation

Studi kasus implementasi nyata alur kerja Agentic QA pada platform pengadaan barang/jasa pemerintah (Tisera Toko Daring).

---

## 1. Konteks Bisnis & Arsitektur
- **Aplikasi:** Tisera Toko Daring (B2G Marketplace).
- **Aktor:**
  1. **Penyedia (Vendor)**: Menjual produk, merespons penawaran & negosiasi harga.
  2. **Pejabat Pengadaan (PP - Buyer)**: Menelusuri katalog, menambahkan ke keranjang, mengikat PPK, membuat pesanan.
  3. **Pejabat Pembuat Komitmen (PPK - Approver)**: Menyetujui hubungan PP-PPK, menyetujui anggaran pesanan, mengesahkan addendum.
- **Total Test Cases:** 590+ TC mencakup fungsional, keamanan, dan integrasi lintas peran.

---

## 2. Penerapan Alur 5 Tahap

### Tahap 1: Ekstraksi PRD & Skenario Awal
Menggunakan BrowserStack Test Companion untuk merekam user journeys:
- Alur pendaftaran produk baru oleh Penyedia.
- Alur checkout belanja instansi oleh PP.
- Alur review & approval oleh PPK.

### Tahap 2: Regresi Otomatis Playwright
- Mengeksekusi rangkaian tes di `tests-penyedia/`, `tests-pp/`, `tests-ppk/`, dan `tests-cross/`.
- Playwright menghasilkan `results.json` dan bukti artifact penangkapan log.

### Tahap 3: Audit Domain (Aturan Pajak & Keamanan)
- **Aturan PPN (PP 49/2022)**:
  - Pembelian buku pelajaran umum wajib memuat PPN Rp 0.
  - Pembelian alat tulis kantor (ATK) membebankan PPN 11%.
  - Negosiasi harga yang berhasil disepakati menurunkan Dasar Pengenaan Pajak (DPP).
- **Temuan Auth Security**:
  - Pengujian login dengan password salah (`TC-002 Penyedia`).
  - Sistem mengembalikan status pass palsu di beberapa test dangkal, namun terdeteksi anomali pada respon URL.

### Tahap 4: Klasifikasi Post-Test Laya
Model ML Laya menganalisis `evidence.json`:
- **`authorization_issue`**: Terkonfirmasi pada `TC-002` (Broken Authentication - password salah tetap masuk ke dashboard).
- **`state_desync_between_users`**: Ditemukan pada skenario penolakan pesanan saat status di dashboard PP belum sinkron dengan keputusan PPK.
- **Triage Matrix:**
  - 28 TC masuk kategori **WAJIB QA MANUAL** (fokus pada isu auth bypass dan mismatch approval).
  - 180+ TC masuk kategori **DISARANKAN SAMPLING** (kalkulasi pajak dan transaksi bertingkat).
  - 380+ TC masuk kategori **AUTO PASS CUKUP** (rendering UI dan navigasi dasar).

### Tahap 5: Validasi Manual Terarah (Human-in-the-Loop)
- QA Engineer hanya perlu meluangkan waktu 1-2 jam untuk menguji 28 skenario kritis.
- Seluruh 28 skenario diuji headed di peramban nyata:
  - Celah keamanan `BUG-001` (CWE-287) langsung dilaporkan ke tim backend developer.
  - Sisa 380+ skenario dasar tidak perlu diulang manual, menghemat waktu testing hingga 85%.
