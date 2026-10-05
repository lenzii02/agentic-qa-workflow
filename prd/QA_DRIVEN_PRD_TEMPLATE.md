# QA-Driven Product Requirement Document (PRD) Template

> **Mandat:** Dokumen ini wajib dibaca dan diisi sebelum proses *development* atau *building* dimulai. QA PRD berfokus pada ketahanan sistem, batasan hak akses, validasi input negatif, dan skenario kegagalan, bukan sekadar happy path.

---

## 1. Metadata Proyek & Fitur
- **Nama Fitur / Modul:** [Nama Fitur]
- **Target Target URL/Endpoint:** `https://[domain]/[path]`
- **Versi Rilis / Sprint:** [v1.0.0 / Sprint N]
- **Lead Developer:** [Nama Developer]
- **QA Lead / PIC:** [Nama QA]

---

## 2. Matriks Batasan Aktor & Peran (Role Boundary Matrix)
Setiap endpoint dan antarmuka harus mendefinisikan hak akses secara eksplisit:

| Role / Aktor | Akun Testing (Kredensial) | Akses yang Diizinkan | Akses yang DIBLOKIR (Wajib 401/403) |
|---|---|---|---|
| **Role A (e.g. Creator/Penyedia)** | `user_a@test.id / pass` | Create, Edit Draft, Submit | Approve, Reject, Bypass Status |
| **Role B (e.g. Buyer/PP)** | `user_b@test.id / pass` | View Catalog, Create Order, Nego | Publish Product, Approve Budget |
| **Role C (e.g. Approver/PPK)** | `user_c@test.id / pass` | Approve Order, Reject, Review | Create Product, Edit Vendor Profile |
| **Unauthenticated / Public** | *Tanpa Sesi* | Public Landing, Login Form | Semua internal route (`/dashboard`, `/profil`) |

---

## 3. Matriks Transisi Status (State Transition Machine)
Mendefinisikan perubahan status entitas data dan siapa yang berhak mengubahnya:

```
[Draft] ──(Submit oleh Aktor A)──▶ [Menunggu Review]
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
         [Disetujui / Aktif]                              [Ditolak / Batal]
        (Approve oleh Aktor C)                          (Reject oleh Aktor C)
```

| Status Awal | Aksi / Trigger | Aktor Berwenang | Status Akhir | Validasi Database / Efek Samping |
|---|---|---|---|---|
| `DRAFT` | Submit Form | Aktor A | `PENDING_REVIEW` | Field timestamp `submitted_at` terisi, notifikasi terkirim |
| `PENDING_REVIEW` | Klik Approve | Aktor C | `APPROVED` | Item muncul di katalog aktif; saldo/pagu terpotong |
| `PENDING_REVIEW` | Klik Reject | Aktor C | `REJECTED` | Wajib menyertakan alasan penolakan (`rejection_reason` min 10 char) |
| `APPROVED` | Request Cancel | Aktor B | `CANCEL_REQUESTED`| Menunggu konfirmasi Aktor A |

---

## 4. Aturan Bisnis & Kalkulasi Finansial (Business & Tax Logic)
Sistem wajib mendefinisikan formula perhitungan secara presisi:

1. **Komponen Biaya:**
   $$\text{Total Bayar} = \text{Subtotal Barang} - \text{Diskon} + \text{PPN} + \text{Ongkos Kirim} + \text{Biaya Layanan}$$
2. **Kondisi PPN (Pajak Pertambahan Nilai):**
   - **Kena PPN (11%):** Kategori Barang Kena Pajak (BKP) & Vendor berstatus PKP.
   - **Bebas PPN (0%):** Kategori Non-BKP (e.g., Buku Pelajaran sesuai PP 49/2022) atau Vendor Non-PKP.
   - **Harga Nego:** Jika harga dinegosiasikan, PPN **wajib** dihitung dari harga kesepakatan akhir.
3. **Pembulatan:** Pembulatan standar keuangan ke satuan Rupiah terdekat (tanpa desimal melayang).

---

## 5. Validasi Input & Negative Requirements (Field-Level)

| Field Name | Tipe Data | Wajib? | Aturan Validasi | Respons Sistem saat Invalid |
|---|---|---|---|---|
| `email` | String | Ya | Format RFC 5322, domain valid | Error text: *"Format email tidak valid"* |
| `password` | String | Ya | Min 8 char, kombinasi huruf & angka | Error text: *"Kata sandi minimal 8 karakter"* |
| `harga` | Numeric | Ya | Min Rp 1.000, Max Rp 10.000.000.000 | Input disanitasi, tidak boleh minus/huruf |
| `file_upload` | File | Opsional | Format: PDF/JPG/PNG, Max Size 5MB | Error alert jika format/ukuran tidak cocok |
| `search_query` | String | Opsional | Strip HTML tags, escape special chars | Mencegah reflected XSS (`<script>`) |

---

## 6. Skenario Pengujian Kritis (Acceptance Criteria - Gherkin)

### Skenario 1: Negative Path — Auth Bypass Prevention
```gherkin
Scenario: Pengguna memasukkan kata sandi yang salah
  Given Pengguna membuka halaman login
  When Pengguna memasukkan email terdaftar dan kata sandi yang salah
  And Pengguna menekan tombol "Masuk"
  Then Sistem wajib menolak login dengan status HTTP 401
  And Pesan peringatan "Email atau kata sandi salah" harus muncul
  And Pengguna TIDAK boleh diarahkan ke dashboard atau menerima session cookie
```

### Skenario 2: Cross-Role State Verification
```gherkin
Scenario: Persetujuan pesanan oleh Approver
  Given Pesanan berada pada status "Menunggu Approval"
  When Approver menekan tombol "Setujui"
  Then Status pesanan berubah menjadi "Disetujui"
  And Status di dashboard Pembeli otomatis terupdate saat di-refresh
  And Vendor menerima notifikasi bahwa pesanan telah disetujui
```

### Skenario 3: Conditional Tax Verification
```gherkin
Scenario: Checkout produk kategori Buku Pelajaran (Bebas PPN)
  Given Pembeli menambahkan produk kategori buku pelajaran ke keranjang
  When Pembeli menuju halaman ringkasan pembayaran
  Then Kolom PPN harus menampilkan nominal Rp 0
  And Total bayar sama dengan subtotal barang ditambah ongkos kirim
```

---

## 7. Exit Criteria / Definition of Done (DoD)
- [ ] Seluruh skenario happy path lolos uji otomatis Playwright.
- [ ] Seluruh skenario negatif (auth bypass, validation error, XSS) tervalidasi.
- [ ] Evidence JSON telah diproses oleh Laya Classifier tanpa blocker status P0/P1.
- [ ] Skenario kategori `WAJIB QA MANUAL` telah dieksekusi secara langsung oleh QA Engineer.
- [ ] Bug report telah terbit untuk seluruh defect yang ditemukan.
