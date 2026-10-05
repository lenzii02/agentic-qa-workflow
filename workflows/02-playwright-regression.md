# Phase 2: Automated Regression & Evidence Harvesting

## 1. Tujuan
Mengeksekusi rangkaian tes regresi otomatis skala besar (ratusan test case) menggunakan Playwright CLI atau Playwright MCP, serta merekam evidence struktural yang dapat dianalisis pada tahap berikutnya.

---

## 2. Praktik Terbaik Penulisan Playwright Spec

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
