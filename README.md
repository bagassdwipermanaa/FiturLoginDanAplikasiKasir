# 🛒 Aplikasi Kasir & Login UKK RPL

Aplikasi sederhana berbasis Desktop (GUI) menggunakan Python untuk memenuhi tugas Praktik UKK (Ujian Kompetensi Keahlian) RPL. Program ini mencakup simulasi fitur login, input data transaksi, validasi, dan cetak invoice struk belanja.

## 📋 Deskripsi Project
Project ini dibuat untuk menyelesaikan studi kasus:
1. **Login System:** Membatasi akses masuk aplikasi.
2. **Input Transaksi:** Memasukkan nama barang, jumlah, dan harga.
3. **Validasi Data:** Mencegah input selain angka pada field nominal.
4. **Invoice Generator:** Menghasilkan output struk belanja yang mendetail.

## 🚀 Fitur Utama
* **GUI User Friendly:** Tampilan antarmuka menggunakan library `tkinter` bawaan Python.
* **Secure Login:** Sistem autentikasi sederhana sebelum masuk menu utama.
* **Auto Calculation:** Menghitung Total Harga dan Uang Kembali secara otomatis.
* **Error Handling:** Menampilkan pesan error jika user salah memasukkan tipe data (huruf di kolom angka).
* **Exact Invoice Output:** Format output struk belanja disesuaikan presisi dengan soal ujian.

## 🛠️ Teknologi yang Digunakan
* **Bahasa:** [Python 3.x](https://www.python.org/)
* **Library GUI:** `tkinter` (Standard Library)
* **IDE:** Visual Studio Code

## 💻 Cara Menjalankan (How to Run)

1. Pastikan Python sudah terinstall di komputer.
2. Buka folder project ini di **VS Code**.
3. Buka file `FiturLoginDanAplikasiKasir.py`.
4. Jalankan perintah berikut di terminal (atau tekan tombol Play):
   ```bash
   python FiturLoginDanAplikasiKasir.py