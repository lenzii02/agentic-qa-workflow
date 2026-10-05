# Defect / Bug Report Template

---

## 1. Ringkasan Singkat (Summary)
- **Bug ID:** `BUG-XXX`
- **Judul:** [Modul] - [Deskripsi Masalah secara Singkat]
- **Target URL / Halaman:** `https://[environment]/[path]`
- **Role Akun Terdampak:** [Buyer / Vendor / Approver / Admin]
- **Severity:** [Critical / Major / Medium / Minor]
- **Priority:** [P0 - Blocker / P1 - High / P2 - Medium / P3 - Low]
- **Kategori Kelemahan (CWE / OWASP):** [e.g. CWE-287: Improper Authentication / OWASP A07:2021]
- **Referensi Test Case:** `[TC-ID]`

---

## 2. Langkah Mereproduksi (Steps to Reproduce)
1. Akses halaman `https://...`
2. Masukkan data: `...`
3. Lakukan tindakan: `...`
4. Amati respons sistem.

---

## 3. Hasil yang Diharapkan (Expected Result)
- [Jelaskan apa yang seharusnya terjadi sesuai PRD atau standar sistem]
- Contoh: Sistem menampilkan error alert *"Password salah"* (HTTP 401) dan tetap berada di form login.

---

## 4. Hasil Aktual (Actual Result)
- [Jelaskan apa yang salah terjadi di aplikasi]
- Contoh: Sistem menerima password salah (HTTP 200/302), menerbitkan session cookie, dan mengarahkan pengguna ke dasbor internal.

---

## 5. Dampak Bisnis & Risiko Teknis (Impact Analysis)
- **Dampak Bisnis:** [Potensi kerugian finansial, manipulasi data, atau pelanggaran regulasi]
- **Risiko Teknis:** [Account Takeover, Injeksi data, atau ketidaksinkronan database]

---

## 6. Bukti Pendukung (Evidence)
- **Screenshot / Screen Recording:** `[Lampiran Gambar/Video]`
- **Console Log / HTTP Payload:**
  ```text
  POST /api/login HTTP/1.1
  Status: 200 OK
  Set-Cookie: session_token=abc123xyz;
  ```

---

## 7. Saran Perbaikan & Root Cause (Remediation)
- **Dugaan Root Cause:** [e.g. Backend controller tidak memanggil fungsi hashing password_verify()]
- **Rekomendasi Fix:** [e.g. Tambahkan validasi hash bcrypt sebelum menerbitkan sesi token]
