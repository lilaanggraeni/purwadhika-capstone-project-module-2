# Sistem Manajemen Stok Barang FMCG

## Deskripsi Proyek
Proyek ini adalah aplikasi berbasis CLI (Command Line Interface) untuk mengelola inventaris barang Fast Moving Consumer Goods (FMCG). Aplikasi menyediakan fungsionalitas CRUD (Create, Read, Update, Delete) untuk pengelolaan data barang.

## Fitur
- **Melihat Data Barang**:
  - Lihat semua barang
  - Filter berdasarkan kategori
  - Cari barang berdasarkan kode

- **Menambah Barang Baru**:
  - Validasi kode barang (format Fxxx)
  - Input informasi lengkap (nama, kategori, stok, satuan, harga, lokasi, supplier)
  - Kategori baru dapat ditambahkan

- **Memperbarui Data Barang**:
  - Update informasi spesifik (nama, kategori, stok, satuan, harga, lokasi, supplier)
  - Validasi untuk setiap input

- **Menghapus Data Barang**:
  - Penghapusan dengan konfirmasi

## Data yang Disimpan
Untuk setiap barang, informasi yang disimpan meliputi:
- Kode barang (format Fxxx)
- Nama barang
- Kategori
- Jumlah stok
- Satuan (rcg/ctn)
- Harga
- Lokasi penyimpanan
- Supplier

## Cara Penggunaan
1. Jalankan program dengan perintah `python assignment2.py`
2. Pilih menu yang diinginkan dengan memasukkan angka yang sesuai
3. Ikuti instruksi pada layar untuk menjalankan fungsi yang diinginkan
4. Untuk keluar dari program, pilih opsi '0' pada menu utama

## Kebutuhan Sistem
- Python 3.x

## Contoh Data
Program ini sudah dilengkapi dengan 20 data barang FMCG sebagai contoh, mencakup kategori:
- Pembersih
- Perawatan
- Bahan Makanan
- Minuman
- Makanan Instan
- Bumbu Masak

## Capstone Project - Module 2
Proyek ini adalah bagian dari Capstone Project untuk Module 2 kursus Purwadhika.