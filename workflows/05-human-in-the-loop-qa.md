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

## 4. Sinkronisasi Otomatis via Google Sheets MCP

Gunakan **Google Sheets MCP** untuk mengunggah dan menyinkronkan seluruh hasil evaluasi tanpa copy-paste manual:
1. **Konfigurasi MCP Server:**
   Pastikan MCP server `google-sheets` terpasang di file konfigurasi agent (`mcp.json`):
   ```json
   {
     "mcpServers": {
       "google-sheets": {
         "command": "node",
         "args": ["D:/Magang/google-sheets-mcp/build/index.js"],
         "env": {
           "GOOGLE_SERVICE_ACCOUNT_KEY_PATH": "D:/Magang/google-sheets-mcp/service-account.json"
         }
       }
     }
   }
   ```
2. **Aksi Sinkronisasi MCP:**
   - Agent memanggil tool `google-sheets.append_rows` atau `google-sheets.update_cells` untuk menulis baris hasil triage Laya.
   - Kolom yang diupdate: `TC ID`, `Status`, `Actual Result`, `Laya Recommendation`, `PIC QA`, `Bug ID`, `Timestamp`.
   - Menjamin bahwa dashboard tracking stakeholder selalu mencerminkan status pengujian terbaru secara real-time.
