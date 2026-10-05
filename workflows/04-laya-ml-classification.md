# Phase 4: Laya Decision Model (Post-Test ML Triage)

## 1. Konsep & Filosofi
**Laya Decision Model** adalah mesin pengambil keputusan post-test berbasis AI/ML (`convaiinnovations/laya`). Laya bertugas mengevaluasi `evidence.json` yang dihasilkan dari eksekusi Playwright MCP dan audit Agent Skill. Laya menganalisis jejak eksekusi, pesan log, HTTP status, dan perbandingan antara ekspektasi dan realita pengujian untuk menghilangkan fenomena *false-pass* (status hijau palsu).

---

## 2. Skema Klasifikasi Laya

Laya memetakan setiap test case ke dalam 5 kategori:

1. **`integration_success`**:
   - Status Playwright passed.
   - Evidence log sinkron dan URL transisi tepat.
   - Tidak ada indikasi kebocoran sesi atau anomali.
2. **`state_desync_between_users`**:
   - Satu pengguna melakukan aksi, namun data tidak terefleksi pada pengguna peran lainnya.
   - Terjadi penundaan sinkronisasi database atau webhook gagal terpicu.
3. **`authorization_issue`**:
   - Bypass login (misal: password salah tetapi tetap dapat mengakses dasbor).
   - Akses rute tanpa batasan peran yang valid.
4. **`critical_blocker`**:
   - Error 500 internal server, deadlock, crashing UI, atau dead-link peramban.
5. **`needs_human_review`**:
   - Evidence log tidak lengkap, selector hilang, atau ketidaksesuaian teks ekspektasi.

---

## 3. Matriks Triage Validasi QA

Berdasarkan hasil klasifikasi Laya dan status otomasi, test case dibagi ke dalam 3 level tindakan:

| Level Triage | Kondisi Pemicu | Tindakan QA |
|---|---|---|
| 🔴 **WAJIB QA MANUAL** | Status FAIL, Authorization Issue, Critical Blocker, atau evidence mismatch | QA wajib mereproduksi manual di browser interaktif |
| 🟡 **DISARANKAN SAMPLING** | Transisi approval multi-role, kalkulasi nominal/PPN, ekspor/unduh file | QA melakukan uji sampling acak 10-20% |
| 🟢 **AUTO PASS CUKUP** | Test case lolos dengan evidence lengkap tanpa ada anomali log | Cukup mengandalkan hasil otomasi |
