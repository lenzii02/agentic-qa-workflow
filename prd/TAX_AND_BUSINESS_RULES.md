# Panduan Audit Aturan Bisnis & Perpajakan (Tax & Business Logic QA)

Dokumen ini mendokumentasikan tata cara penulisan requirement dan pengujian logika perpajakan dinamis, khususnya untuk platform e-commerce dan e-procurement (pemerintah/B2G).

---

## 1. Aturan Dasar PPN (Pajak Pertambahan Nilai)

Di sistem pengadaan pemerintah dan marketplace Indonesia:
1. Tarif PPN standar umum adalah **11%** (mengacu UU Harmonisasi Peraturan Perpajakan / HPP).
2. **Kondisi Bebas PPN (0%):**
   - Berdasarkan **PP No. 49 Tahun 2022**, barang-barang tertentu dibebaskan dari pengenaan PPN:
     - Buku pelajaran umum, kitab suci, buku teks utama.
     - Barang kebutuhan pokok pangan tertentu.
   - Skenario Uji: Produk dalam kategori ini **tidak boleh** membebankan PPN pada rincian keranjang atau checkout.

---

## 2. Matriks Kondisi Perpajakan

| Status Vendor | Kategori Barang | Jenis Transaksi | Tarif PPN | Keterangan & Dasar Regulasi |
|---|---|---|---|---|
| **PKP (Pengusaha Kena Pajak)** | BKP (ATK, Komputer, Furniture) | Standar | 11% | Wajib terbit faktur pajak |
| **PKP** | Non-BKP (Buku Pelajaran Sekolah) | Standar | 0% (Bebas) | Sesuai PP 49/2022 |
| **Non-PKP** | BKP / Non-BKP | Standar | 0% | Vendor Non-PKP tidak berhak memungut PPN |
| **PKP** | BKP | Ada Negosiasi Harga | 11% dari Harga Nego | PPN dihitung dari harga akhir pasca diskon/nego |

---

## 3. Formula Matematika Validasi QA

$$\text{Subtotal Akhir} = \sum (\text{Qty} \times \text{Harga Satuan Akhir})$$

$$\text{DPP (Dasar Pengenaan Pajak)} = \text{Subtotal Akhir} - \text{Diskon Toko}$$

$$\text{Nominal PPN} = 
\begin{cases} 
\text{round}(\text{DPP} \times 0.11), & \text{jika PKP dan Barang Kena Pajak} \\
0, & \text{jika Bebas PPN atau Non-PKP}
\end{cases}$$

$$\text{Total Transaksi} = \text{DPP} + \text{Nominal PPN} + \text{Ongkos Kirim} + \text{Asuransi}$$

---

## 4. Checklist Skenario Pengujian Perpajakan (QA Checklist)

- [ ] **Uji Kategori Buku vs Non-Buku:**
  - Tambahkan 1 item buku pelajaran ke keranjang -> Cek nilai PPN = Rp 0.
  - Tambahkan 1 item pulpen (BKP) ke keranjang yang sama -> Cek PPN = 11% hanya dari subtotal pulpen.
- [ ] **Uji Perubahan Harga Negosiasi:**
  - Harga awal katalog Rp 1.000.000 (PPN 110.000).
  - Nego disepakati Rp 800.000.
  - Pastikan nilai PPN otomatis turun menjadi Rp 88.000 (bukan tetap 110.000).
- [ ] **Uji Ekspor Invoice & PDF:**
  - Unduh cetakan invoice/faktur pesanan.
  - Pastikan angka nominal PPN di antarmuka web persis sama dengan yang tertera pada file PDF/Excel (tidak ada selisih pembulatan floating point).
- [ ] **Uji Akun Vendor Non-PKP:**
  - Beli produk dari akun toko yang belum berstatus PKP.
  - Baris PPN harus bernilai Rp 0 atau tertulis *"Tidak Dipungut (Non-PKP)"*.
