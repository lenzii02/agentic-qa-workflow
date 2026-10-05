# Phase 3: Agent Skill (Coverage, Cross-Testing, Rumus, & Bug Report)

## 1. Tujuan
Memanfaatkan keahlian penalaran mendalam AI Agent melalui **Agent Skill** untuk menyelesaikan 4 tugas krusial yang tidak bisa dilakukan oleh skrip Playwright biasa:
1. **Coverage Gap Analysis**
2. **Cross-Role Testing**
3. **Audit Rumus Bisnis & Perpajakan (PPN/PPh)**
4. **Standardized Bug Reporting**

---

## 2. 4 Pilar Kemampuan Agent Skill

### A. Coverage Gap Analysis
- Membandingkan daftar test cases dari Phase 1 & 2 dengan matriks PRD (`prd/QA_DRIVEN_PRD_TEMPLATE.md`).
- Menemukan skenario yang belum teruji:
  - Form validation dengan field kosong atau karakter Unicode aneh.
  - Skenario batas timeout jaringan (slow 3G / network failure).
  - Kasus batas otorisasi (401 Unauthorized / 403 Forbidden).

### B. Cross-Role Testing (Multi-Actor Orchestration)
- Mengorkestrasi interaksi berantai yang melibatkan lebih dari satu pengguna/peran:
  1. **Aktor A (Penyedia/Vendor):** Buat dan daftarkan produk baru atau submit penawaran harga.
  2. **Aktor B (Pembeli/PP):** Cari produk di katalog, masukkan ke keranjang belanja, ajukan pesanan.
  3. **Aktor C (Approver/PPK):** Buka daftar persetujuan, review rincian anggaran, setujui atau tolak pesanan.
  4. **Aktor B & A:** Verifikasi pembaruan status transaksi secara real-time.

### C. Audit Rumus Bisnis & Perpajakan (PPN / DPP)
- Memverifikasi formula matematika secara presisi:
  - **PPN 11% vs Bebas PPN (0%)**: Kategori Barang Kena Pajak (BKP) dikenakan PPN 11%; Kategori Non-BKP (seperti buku pelajaran umum atau kitab suci berdasarkan PP 49/2022) bebas PPN.
  - **Dasar Pengenaan Pajak (DPP)**: Dipastikan dihitung dari harga akhir kesepakatan setelah negosiasi atau diskon, bukan harga awal katalog.
  - **Ongkos Kirim & Asuransi**: Memvalidasi apakah ongkos kirim kena pajak atau terpisah.
  - **Pembulatan Desimal**: Memastikan tidak ada selisih Rp 1 akibat pembulatan *floating point*.

### D. Standardized Bug Reporting (OWASP / CWE)
- Jika ditemukan anomali atau kegagalan, Agent Skill menyusun laporan cacat dengan format baku:
  - Severity & Priority terukur.
  - Mapping ke CWE / OWASP Top 10 (misal: CWE-287 untuk login bypass, CWE-862 untuk missing auth).
  - Langkah reproduksi deterministik.
  - Expected vs Actual evidence (URL, DOM text, HTTP status, request payload).

---

## 3. Output Tahap Audit

Agent menghasilkan catatan verifikasi awal dan rekomendasi skenario tambahan yang perlu dimasukkan ke dalam evidence sebelum diproses oleh classifier model ML.
