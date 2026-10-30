# 📱 Panduan Lengkap Bot Auto Create Gmail (Metode Baru: Bypass Ganti Umur)

Panduan ini diperbarui sesuai dengan metode terbaru (video 4 menit): **Bypass Akun Anak (Family Link Parent Sign-In) -> Back ke Menu Umur Dewasa (2001 - 2008) -> Gmail Market Jadi & Kirim Telegram**.

---

## 1. Mengapa Metode YouTube Sudah Tidak Dipakai?
Metode lama via YouTube Kids sudah ditutup/diperketat oleh Google.  
Metode baru ini **jauh lebih cepat, simpel, dan tembus tanpa verifikasi nomor HP** dengan memanfaatkan celah *Parental Consent Bypass*:
1. Mendaftar akun Google dengan opsi **"For my child" (Untuk anak saya)**.
2. Memasukkan tahun lahir anak (**2015**).
3. Masuk ke halaman **"Parent sign-in"** -> Masukkan email orang tua (`by.u001user@gmail.com`) dan password ortu (`martabakmesir13`).
4. Centang persetujuan orang tua hingga masuk konfirmasi.
5. **Kunci Trik (Bypass):** Tekan tombol **BACK** beberapa kali hingga kembali ke halaman **"Basic information" (Tanggal Lahir)**.
6. Ubah tahun lahir menjadi umur dewasa (**2001 s/d 2008**).
7. Klik **Next** -> Google otomatis mengubah akun menjadi Akun Dewasa Mandiri (lepas dari Family Link) tanpa meminta nomor HP!
8. Masukkan alamat Gmail Market yang diinginkan & Password Market (`sgsg1122` / `goldacok` / custom).
9. Akun langsung aktif, dan kredensial otomatis terkirim ke Telegram!

---

## 2. Fitur Baru di Skrip `auto_create_gmail.js`
1. **Form Konfigurasi Lengkap**:
   - **Email & Password Ortu**: Sudah default `by.u001user@gmail.com` dan `martabakmesir13` (bisa diedit jika ingin ganti akun ortu lain).
   - **Password Gmail Market**:
     - Pilihan tombol cepat: `sgsg1122` atau `goldacok`.
     - Opsi isi password sendiri jika ingin request password lain.
   - **Pilihan Tahun Dewasa**:
     - Rekomendasi: Fix Tahun **2001** (paling stabil).
     - Opsi Random Tahun: **2001 s/d 2008**.
   - **Kirim Telegram Otomatis**: Hasil email market & password yang sudah fix langsung dikirimkan ke chat/bot Telegram Anda.
   - **Pilihan Browser**: Support *Samsung Internet Browser* dan *Google Chrome*.
   - **Support Dwi Bahasa**: Teks selector mendukung HP berbahasa Inggris maupun Indonesia.

---

## 3. Langkah Penggunaan di HP Android

### Langkah 1: Pengaturan Awal di HP
1. Pastikan aplikasi **AutoX.js** sudah terinstal di HP Android.
   - [Download AutoX.js v6 APK (GitHub Releases)](https://github.com/kkevsekk1/AutoX/releases)
2. Buka AutoX.js dan aktifkan:
   - **Layanan Aksesibilitas (Accessibility Service)**: Masuk ke *Pengaturan HP > Aksesibilitas > Layanan yang Didownload > AutoX.js > Aktifkan*.
   - **Izin Floating Window (Jendela Mengambang)**.

### Langkah 2: Impor Skrip ke AutoX.js
1. Kirim file [`auto_create_gmail.js`](file:///c:/xampp/htdocs/auto-create-email/auto_create_gmail.js) ke HP Anda.
2. Di AutoX.js, klik tanda **`+`** di pojok kanan bawah -> Pilih **Import** -> Pilih file `auto_create_gmail.js`.

### Langkah 3: Menjalankan Bot
1. Klik tombol **Run** (segitiga hijau) pada file `auto_create_gmail.js`.
2. Form pengaturan akan muncul:
   - Cek Email & Password Ortu (sudah otomatis terisi `by.u001user@gmail.com` & `martabakmesir13`).
   - Pilih Password Akun Jadi: Klik `sgsg1122` atau `goldacok` (atau ketik sendiri).
   - Pilih Tahun Dewasa: `2001` (Rekomendasi).
   - Masukkan Token & Chat ID Telegram Anda.
3. Klik tombol hijau **"MULAI OTOMASI ALUR BARU"**.
4. Bot akan otomatis bekerja di browser sampai selesai dan mengirimkan hasilnya ke Telegram!

---

## 4. Cara Menghubungkan ke Telegram Bot Anda
Agar setiap email yang selesai langsung masuk ke Telegram:
1. **Bot Token**: Dapatkan dari bot **@BotFather** di Telegram (ketik `/newbot`).
2. **Chat ID**: Dapatkan dari bot **@userinfobot** di Telegram (ketik `/start`).
3. Masukkan ke kolom Token dan Chat ID pada aplikasi bot sebelum klik mulai.
