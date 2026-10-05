# Phase 2: Playwright MCP (Status & Actual Result Collection)

## 1. Tujuan
Mengeksekusi rangkaian tes regresi otomatis skala besar menggunakan **Playwright MCP (Model Context Protocol)** secara headless maupun headed, untuk mengumpulkan `Status` (Passed/Failed) dan `Actual Evidence` yang objektif dari peramban.

---

## 2. Peran Playwright MCP
- **Protokol:** Model Context Protocol (MCP) server `playwright`
- **Fungsi Utama:**
  1. Mengontrol instance Chromium/WebKit/Firefox langsung dari AI Agent.
  2. Menangkap **Status Eksekusi**: `passed`, `failed`, `timedOut`, `skipped`.
  3. Merekam **Actual Result Nyata**:
     - Current URL setelah navigasi/redirect.
     - Cuplikan pesan teks aktual pada modal atau alert box.
     - Network request status (200, 401, 403, 500).
     - Browser console errors & warnings.
     - DOM snapshots & screenshot path saat assertion gagal.

---

## 3. Praktik Terbaik Penulisan Playwright Spec

1. **Struktur Modular per Peran / Modul:**
   ```text
   tests/
   ├── role-a/
   │   ├── 01-login.spec.ts
   │   └── 02-dashboard.spec.ts
   ├── role-b/
   │   └── 01-checkout.spec.ts
   └── cross-role/
       └── 01-order-approval.spec.ts
   ```
2. **Assertion Mendalam (Deep Assertions):**
   - Hindari sekadar memeriksa `toBeVisible()`.
   - Lakukan assertion terhadap teks status database, pesan konfirmasi, dan URL akhir:
     ```typescript
     // Kurang kuat
     await expect(page.locator('.alert-success')).toBeVisible();

     // Direkomendasikan
     await expect(page.locator('.alert-success')).toContainText('Pesanan berhasil diajukan');
     await expect(page).toHaveURL(/.*\/pesanan\/detail\/\d+/);
     ```
3. **Konfigurasi Reporter:**
   Pastikan Playwright mengekspor hasil dalam bentuk JSON reporter untuk agregasi evidence:
   ```bash
   npx playwright test --reporter=list,json
   ```
   Hasil akan tersimpan di `test-results/results.json`.

---

## 3. Ekstraksi Evidence (`evidence.json`)

Eksekusi script `scripts/build-evidence.mjs` untuk mengonversi hasil mentah Playwright menjadi evidence terstruktur:
- Menangkap HTTP status code, URL tujuan, durasi eksekusi, console errors, dan cuplikan log.
- Memasangkan hasil eksekusi aktual dengan `Expected Result` dari draf CSV.
