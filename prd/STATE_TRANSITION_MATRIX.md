# Panduan Matriks Transisi Status Multi-Peran (State Transition Matrix)

Dokumen ini adalah template standar untuk memetakan alur transaksi kompleks multi-aktor (misal: Supplier → Buyer → Approver → Finance).

---

## 1. Format Tabel State Machine

| Entity | State Saat Ini | Aksi / Event | Actor Yang Berhak | Guard Condition | State Berikutnya | Efek Samping (Side Effects) |
|---|---|---|---|---|---|---|
| **Produk** | `DRAFT` | Submit Produk | Supplier | Form wajib lengkap, foto terunggah | `WAITING_APPROVAL` | Notifikasi ke Approver, belum tampil di publik |
| **Produk** | `WAITING_APPROVAL` | Approve | Approver | - | `ACTIVE` | Muncul di katalog pencarian |
| **Produk** | `WAITING_APPROVAL` | Reject | Approver | Alasan tolak terisi min 10 karakter | `REJECTED` | Notifikasi ke Supplier beserta alasan |
| **Pesanan** | `CART` | Checkout | Buyer | Ada alamat kirim, ada PPK terpilih | `WAITING_PAYMENT` / `WAITING_APPROVAL` | Stok produk ter-reserve |
| **Pesanan** | `WAITING_APPROVAL` | Approve Order | Approver | Sisa pagu anggaran mencukupi | `ORDER_CONFIRMED` | Pagu terpotong, pesanan masuk ke Supplier |
| **Pesanan** | `ORDER_CONFIRMED` | Kirim Barang | Supplier | Nomor resi terisi | `SHIPPED` | Tracking resi aktif |
| **Pesanan** | `SHIPPED` | Terima Barang & Selesai | Buyer | Konfirmasi barang sesuai | `COMPLETED` | BAST tercetak, pencairan dana terbuka |
| **Pesanan** | `SHIPPED` | Ajukan Komplain | Buyer | Lampiran bukti foto/video ada | `COMPLAINT_OPEN` | Status pembayaran di-hold |

---

## 2. Checklist Verifikasi QA untuk State Transitions

1. **Unauthorized Transition (Bypass Test)**:
   - Coba ubah state secara langsung lewat request API tanpa melalui actor yang berwenang.
   - Contoh: Apakah Supplier bisa langsung memanggil endpoint `/api/order/approve`? Sistem harus mengembalikan `403 Forbidden`.
2. **Invalid State Transition (Skip Step Test)**:
   - Coba lompat dari `DRAFT` langsung ke `COMPLETED` tanpa melalui approval atau payment.
3. **Idempotency & Race Condition**:
   - Double-click tombol "Approve" atau "Submit" secara cepat.
   - Sistem wajib menangani request kedua dengan aman (idempotency key atau database lock), tidak boleh membuat transaksi ganda.
4. **Data Sync Antar Sesi**:
   - Ketika Aktor A melakukan perubahan state di jendela peramban miliknya, pastikan saat Aktor B me-refresh halamannya, status data baru langsung terrefleksi.
