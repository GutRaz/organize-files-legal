> **Versi bahasa Indonesia.** Jika terjadi konflik, versi [bahasa Inggris](./DATA_DELETION.md) yang berlaku.

---

# Penghapusan Data — Organize Files

**Organize Files** memproses file Anda **secara lokal di perangkat Anda**.
Penerbit **tidak** mengoperasikan sistem akun dan **tidak** menyimpan file Anda di
servernya sendiri selama operasi pengorganisasian atau perbaikan biasa. Karena
tidak ada akun di sisi server, sebagian besar data Anda tidak pernah meninggalkan
perangkat dan Anda tetap memegang kendali penuh atasnya.

Halaman ini menjelaskan cara menghapus data yang disimpan aplikasi di perangkat
Anda, serta data terbatas yang mungkin disimpan penerbit.

## Data yang disimpan di perangkat Anda

Aplikasi menyimpan data kerja lokal seperti snapshot sesi, status pelanjutan, log
opsional, status uji coba/lisensi, dan — hanya jika Anda mengaktifkan notifikasi
email — kata sandi SMTP terenkripsi. Anda dapat menghapusnya kapan saja:

1. **Hapus data aplikasi** — buka aplikasi dan gunakan **Hapus data aplikasi**.
   Ini menghapus sesi, log, dan draf otomatisasi. Ini mungkin mempertahankan
   status lisensi lokal dan pengenal instalasi yang digunakan untuk
   pemeriksaan lisensi opsional; konfirmasi di dalam aplikasi menjelaskan dengan
   tepat apa yang dipertahankan.
2. **Copot pemasangan aplikasi** — menghapus aplikasi akan menghapus penyimpanan
   pribadinya di perangkat seluler. Di desktop, Anda juga dapat menghapus folder
   profil secara manual:
   - Windows: `%LocalAppData%\OrganizeFilesCrossPlatform\`
   - Linux / macOS: folder profil aplikasi di direktori beranda Anda
3. **Hapus folder keluaran** — file terorganisir atau diperbaiki yang Anda buat
   akan tetap ada sampai Anda menghapusnya sendiri.

## Data yang mungkin disimpan penerbit

Penerbit hanya menyimpan data yang Anda kirim secara aktif, seperti:

- Korespondensi **email dukungan**, jika Anda menghubungi dukungan
- **Catatan server lisensi**, hanya jika server lisensi dikonfigurasi untuk build
  Anda

Untuk meminta penghapusan data ini, kirim email ke **razvan.gutulov@outlook.com**
dengan menyertakan:

- Alamat email yang Anda gunakan untuk menghubungi dukungan, dan/atau
- Referensi lisensi atau pesanan Anda, jika ada

Penerbit berupaya menanggapi dalam **30 hari** setelah permintaan diverifikasi.
Beberapa catatan dapat disimpan jika diwajibkan oleh hukum (misalnya catatan pajak
dan akuntansi). Lihat [Kebijakan Privasi](./PRIVACY_POLICY_ID.md) untuk detail
lengkap tentang penyimpanan.

## Pembelian di toko

Pembelian dan penagihan ditangani oleh toko tempat Anda membeli (Microsoft Store,
Google Play, atau Apple App Store). Untuk mengelola atau menghapus data pembelian
yang disimpan toko, gunakan pengaturan akun toko tersebut.

---

© 2026 Razvan Constantin Gutulov. Semua hak dilindungi.
