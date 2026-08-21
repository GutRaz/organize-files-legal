> **Terjemahan mesin tidak resmi — bukan nasihat hukum.** [EULA Bahasa Inggris](./EULA_EN.md) dan [Kebijakan Privasi Bahasa Inggris](./PRIVACY_POLICY_EN.md) mengatur jika terjemahan ini bertentangan dengan keduanya. Konsultasikan dengan penasihat yang berkualifikasi di yurisdiksi Anda.

---

# Kebijakan Privasi — Mengatur File

**Penerbit:** Guțulov Răzvan Constantin PFA  
**Alamat terdaftar:** Str. Republicii nr. 33B, bl. N3, sc. A, et. 1, ap. 3, Breaza de Sus, 105400 Breaza, jud. Prahova, România  
**Daftar perdagangan:** F2026004513003 (EUID ROONRC.F2026004513003)  
**Nomor identifikasi pajak:** 53610310  
**Hubungi:** razvan.gutulov@outlook.com  
**Tanggal efektif:** 28-05-2026  
**URL Publik:** `https://github.com/GutRaz/organize-files-legal/blob/main/PRIVACY_POLICY_ID.md`

---

## Ringkasan

Atur File memproses file **secara lokal di perangkat**. Konten file **tidak diunggah ke server milik penerbit** untuk operasi pengaturan atau perbaikan normal. Aplikasi **menulis file lokal** di perangkat (snapshot sesi, status resume, log opsional) seperti dijelaskan di bawah.

## Data diproses secara lokal

| Data | Dimana disimpan | Tujuan |
|------|----------------|---------|
| File dan folder yang Anda pilih | Hanya perangkat Anda | Atur, hapus duplikat, perbaiki, hapus opsional |
| Cuplikan sesi UI (`last-ui-session.json`) | `%LocalAppData%\OrganizeFilesCrossPlatform\sessions\<id>\` (desktop) atau penyimpanan pribadi aplikasi (Android) | Pulihkan ruang kerja: jalur, ekstensi, opsi |
| Atur resume + jurnal perpindahan opsional | Keluaran `_OrganizeMediaLogs` atau folder sesi | Lewati gerakan yang sudah selesai; metadata pemulihan (jalur yang dikodekan) |
| Opsional menjalankan detak jantung JSON | Keluaran `_OrganizeMediaLogs` | Penghitung kemajuan untuk alat eksternal |
| Status percobaan/lisensi | Folder profil di bawah Data Aplikasi Lokal | Menerapkan hak uji coba atau penyimpanan |
| Perbarui-periksa status | Folder profil | Batasi pemeriksaan manifes versi opsional |
| Pementasan SAF Android | Folder sesi di bawah penyimpanan aplikasi | Salin pohon `konten://` sehingga mesin dapat membacanya |
| Kata sandi SMTP opsional untuk notifikasi email | Disimpan terenkripsi dalam preferensi sesi di perangkat (AES-GCM dengan file kunci per profil). Saat peningkatan, jika bidang ada, kata sandi SMTP lama yang disimpan tanpa AES-GCM ditulis ulang satu kali ke AES-GCM. File kunci AES-GCM tetap berada di folder profil aplikasi dan dapat dibaca oleh akun pengguna OS yang masuk; ini melindungi pembacaan kasual JSON preferensi, bukan brankas berbasis perangkat keras. | Hanya jika notifikasi email diaktifkan dan kredensial SMTP dimasukkan |

## Apa yang tidak diterima penerbit secara default

- Isi file dari proses pengorganisasian/perbaikan  
- Kontak, lokasi, mikrofon, atau kamera (tidak digunakan)  
- SDK Analytics yang dipaketkan dalam pohon sumber terbuka  

## Penggunaan jaringan opsional

| Aktivitas | Data terkirim | Penerima |
|----------|-----------|-----------|
| Pemeriksaan pembaruan opsional | HTTPS GET ke manifes versi. Host (misalnya GitHub) menerima alamat IP permintaan, Agen-Pengguna `OrganizeFiles-UpdateCheck/1.0`, dan metadata TLS. Tidak ada jalur file atau konten file yang dikirim. Nonaktifkan dengan `ORGANIZE_FILES_DISABLE_UPDATE_CHECK=1`. | Host yang menyajikan manifes JSON |
| Pembelian / lisensi toko | API penagihan platform | Microsoft, Google, atau Apple (per saluran) |
| Server lisensi opsional (dikonfigurasi operator) | ID instalasi persisten acak (GUID disimpan di `license_installation_id.txt`) dikirim ke server lisensi yang dioperasikan penerbit atau dikonfigurasi oleh operator di `ORGANIZE_FILES_LICENSE_SERVER_URL`. ID instalasi adalah pengidentifikasi perangkat berdasarkan GDPR Recital 30. Dasar hukum: pelaksanaan kontrak. Retensi yang dioperasikan penerbit: catatan hak selama aktif ditambah hingga 24 bulan setelah kedaluwarsa/pencabutan untuk pencegahan penyalahgunaan dan penanganan sengketa; catatan akuntansi dapat disimpan hingga 7 tahun jika diwajibkan hukum. Server yang dijalankan operator mengikuti jadwal retensi terdokumentasi operator. Fitur ini tidak aktif kecuali `ORGANIZE_FILES_LICENSE_SERVER_URL` disetel. | Server lisensi penerbit atau operator |
| Pelacakan OpenTelemetry opsional (dikonfigurasi operator) | Ketika `ORGANIZE_FILES_OTEL_EXPORTER_OTLP_ENDPOINT` disetel, metadata tugas otomatisasi (ID tugas, ID korelasi, tag jenis target, konteks pelacakan W3C) diekspor ke kolektor OTLP yang dikonfigurasi. Tidak ada jalur file atau konten file yang disertakan. Fitur ini tidak aktif secara default dan memerlukan konfigurasi operator eksplisit. | Kolektor OTLP yang dikonfigurasi oleh operator |
| Notifikasi email opsional (saat diaktifkan) | Status berjalan dan cuplikan log (dapat mencakup jalur file) dikirim melalui server SMTP yang dikonfigurasi operator | SMTP operator / penyedia email |
| Webhook otomatisasi opsional (dikonfigurasi operator) | Ketika `ORGANIZE_FILES_AUTOMATION_WEBHOOK_URL` disetel, peristiwa siklus hidup tugas berisi ID korelasi dan jalur berkas status otomatisasi | Endpoint webhook yang dikonfigurasi operator |
| Pembantu coba lagi NAS mesin | Tidak ada selain jalur jaringan yang dikonfigurasi | Tuan rumah NAS/UKM |

Pemeriksaan pembaruan membandingkan **hanya metadata versi**. Aplikasi desktop dapat menjalankan pemeriksaan ini sekali sehari setelah penerimaan EULA kecuali dinonaktifkan.

## Dasar hukum (pembingkaian bergaya GDPR, bukan nasihat hukum)

| Pemrosesan | Dasar tipikal |
|------------|----------------|
| Penataan/perbaikan lokal pada folder yang sudah dipilih | Kinerja kontrak / kepentingan sah operator |
| File sesi lokal, resume, dan detak jantung | Sama — diperlukan untuk menyediakan alat |
| Simpan penagihan dan hak | Kontrak dengan toko platform |
| Pemeriksaan manifes pembaruan opsional | Kepentingan yang sah terhadap pembaruan keamanan; dapat dinonaktifkan melalui variabel lingkungan |
| Email dukungan | Kepentingan yang sah/langkah pra-kontraktual atas permintaan Anda |

## Transfer internasional

Pemeriksaan pembaruan opsional dapat menjangkau server di luar Wilayah Ekonomi Eropa (misalnya GitHub di Amerika Serikat). Penagihan toko ditangani berdasarkan ketentuan masing-masing platform.

## Otoritas pengawas dan pengaduan

Jika undang-undang yang berlaku memberikan hak subjek data atau keluhan kepada otoritas pengawas, hubungi penerbit terlebih dahulu di **razvan.gutulov@outlook.com**. Penduduk UE/EEA juga dapat mengajukan keluhan kepada otoritas perlindungan data setempat (untuk Rumania: ANSPDCP, https://www.dataprotection.ro).

## Prosesor pihak ketiga (saat fitur ini digunakan)

- **Microsoft Store / Google Play / Mac App Store** — penagihan dan hak. Google Play menggunakan Penagihan di perangkat; listingan produksi harus menambahkan Integritas Play dan/atau verifikasi sisi server sesuai kebijakan Google.
- **GitHub (atau host manifes)** — versi opsional JSON melalui HTTPS (dapat menyertakan IP klien di log server)
- **Klien email** — saat menghubungi dukungan melalui tautan mailto

## Tanggung jawab operator (pembingkaian gaya GDPR)

Data pribadi mungkin ada **di dalam** file Anda. Jika Anda memproses data tersebut, Anda (atau organisasi Anda) mungkin merupakan **pengendali data** dan harus memilih dasar yang sah, meminimalkan retensi, dan menanggapi permintaan subjek data.

## Retensi

File lokal tetap ada sampai Anda menghapusnya, menghapus data aplikasi, menghapus instalan aplikasi, atau menimpa folder keluaran. Penerbit tidak menjalankan jadwal penyimpanan terpusat untuk data lokal saja.

Untuk data yang dipegang penerbit:

- Email dukungan dan korespondensi: hingga 24 bulan setelah kontak bermakna terakhir, kecuali sengketa atau kewajiban hukum memerlukan retensi lebih lama.
- Catatan pembelian langsung, pengembalian dana, pajak, dan akuntansi: hingga 7 tahun jika diwajibkan hukum pajak atau akuntansi.
- Catatan hak pada server lisensi yang dioperasikan penerbit: selama hak aktif ditambah hingga 24 bulan setelah kedaluwarsa atau pencabutan.
- Log akses dan keamanan pada server yang dioperasikan penerbit: hingga 90 hari, kecuali diperlukan lebih lama untuk investigasi keamanan, pencegahan penipuan, atau klaim hukum.


## Hak Anda

Untuk data yang dimiliki penerbit (misalnya korespondensi email dukungan), hubungi **razvan.gutulov@outlook.com**. Untuk data yang hanya disimpan di perangkat, Anda dapat menghapus sebagian besar data aplikasi melalui **Hapus data aplikasi**, mencopot pemasangan, atau menghapus file secara manual. **Hapus data aplikasi** menghapus sesi, log, dan draf otomatisasi, namun dapat mempertahankan jangkar uji coba lisensi, penanda pemasangan berbayar, dan pengidentifikasi pemasangan yang digunakan untuk pemeriksaan lisensi opsional — lihat teks konfirmasi dalam aplikasi sebelum Anda melanjutkan.

## Anak-anak

Alat produktivitas umum tidak ditujukan untuk anak-anak di bawah 13 tahun (atau usia yang diwajibkan di wilayah hukum Anda).

## Perubahan

Perubahan penting akan muncul di listingan toko dan dokumentasi dalam aplikasi sebelum rilis.

## Dokumen terkait

- [EULA (Bahasa Inggris)](./EULA_ID.md)  
- [Kebijakan privasi (Rumania)](./PRIVACY_POLICY_RO.md)  
- [Kebijakan privasi (Jerman)](./PRIVACY_POLICY_DE.md)  
- [Kebijakan privasi (Prancis)](./PRIVACY_POLICY_FR.md)

---

Jika terjemahan ini tidak lengkap, Kebijakan Privasi bahasa Inggris yang berlaku.

## Pengendali dan kontak

Untuk data pribadi yang diproses oleh penerbit, pengendalinya adalah **Guțulov Răzvan Constantin PFA**. Kontak: **razvan.gutulov@outlook.com**.

## Retensi (catatan penerbit)

Untuk data yang disimpan oleh penerbit:

- Email dukungan dan korespondensi: hingga 24 bulan setelah kontak bermakna terakhir, kecuali sengketa atau kewajiban hukum memerlukan retensi lebih lama.
- Catatan pembelian langsung, pengembalian dana, pajak, dan akuntansi: hingga 7 tahun jika diwajibkan oleh hukum pajak atau akuntansi.
- Catatan hak pada server lisensi yang dioperasikan penerbit: selama hak aktif ditambah hingga 24 bulan setelah kedaluwarsa atau pencabutan.
- Log akses dan keamanan pada server yang dioperasikan penerbit: hingga 90 hari, kecuali diperlukan lebih lama untuk investigasi keamanan, pencegahan penipuan, atau klaim hukum.

## Hak Anda (waktu respons)

Penerbit berupaya menanggapi permintaan subjek data dalam **30 hari** setelah permintaan terverifikasi (verifikasi identitas dapat diminta bila wajar diperlukan).
