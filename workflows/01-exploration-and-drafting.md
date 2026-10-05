# Phase 1: Exploration & Initial Test Case Generation

## 1. Tujuan
Memetakan seluruh antarmuka web, user journeys, elemen interaktif, dan menghasilkan draf awal Test Cases secara cepat menggunakan ekstensi peramban cerdas (BrowserStack Test Companion / AI Extension).

---

## 2. Langkah Kerja

1. **Aktivasi Companion / AI Crawler**:
   - Buka aplikasi web di lingkungan staging/dev.
   - Aktifkan perekaman atau navigasi cerdas pada peramban.
2. **Jelajahi Jalur Pengguna Utama (Core Journeys)**:
   - Akses setiap modul mulai dari navigasi menu, formulir input, filter tabel, hingga alur checkout.
   - Uji dengan berbagai tipe akun (Multi-Role Exploration).
3. **Ekstraksi Hasil ke Format Standar**:
   - Simpan draf test case ke dalam file CSV mengikuti skema:
     `TC ID`, `Module`, `Scenario`, `Precondition`, `Steps`, `Test Data`, `Expected Result`, `Test Type`.

---

## 3. Aturan Pembersihan Draf (Refinement Rules)

Draf hasil generate otomatis sering kali terlalu dangkal (hanya memverifikasi rendering elemen visual). QA Engineer wajib melakukan kurasi:
- **Hapus Redundansi:** Gabungkan pengujian klik tombol yang serupa menjadi satu skenario komprehensif.
- **Tambahkan Skenario Negatif:** Jika AI hanya membuat skenario *"Login dengan akun valid"*, tambahkan *"Login dengan password salah"*, *"Login dengan format email rusak"*, dan *"Login dengan akun terblokir"*.
- **Tetapkan Parameter Unik:** Gunakan placeholder dinamis untuk data uji (misal: `test_{timestamp}@domain.com`) untuk menghindari duplikasi data di lingkungan staging.
