# Sistem Manajemen Stok Barang FMCG

## Deskripsi Program
Program ini adalah aplikasi berbasis CLI (Command Line Interface) untuk mengelola inventaris barang Fast Moving Consumer Goods (FMCG). Program ini menyediakan fungsionalitas CRUD (Create, Read, Update, Delete) untuk pengelolaan data barang.

## Urgensi Program
1. Efisiensi Operasional:
   - Mengurangi kesalahan pencatatan manual
   - Mempercepat proses pencarian dan update stok
   - Memudahkan tracking lokasi barang
2. Kontrol Inventori:
   - Mencegah stockout dan overstock
   - Memantau pergerakan barang dengan mudah
   - Mengurangi risiko kehilangan barang
3. Pengambilan Keputusan:
   - Data real-time untuk keputusan pembelian
   - Analisis kategori produk yang efektif
   - Optimalisasi ruang penyimpanan

## Stakeholder
1. **Manajer Gudang**
   - Bertanggung jawab atas pengelolaan inventaris
   - Membutuhkan akses penuh untuk monitoring stok
   - Membutuhkan laporan terkini tentang status barang

2. **Staff Gudang**
   - Melakukan input data barang baru
   - Mengupdate informasi stok
   - Melakukan pencarian dan filter data

3. **Tim Keuangan**
   - Membutuhkan informasi harga dan nilai inventaris
   - Menggunakan data untuk perhitungan aset

4. **Tim Marketing**
   - Membutuhkan informasi tentang ketersediaan produk
   - Menggunakan data untuk perencanaan kampanye

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