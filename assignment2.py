# SISTEM MANAJEMEN STOK BARANG FMCG
# Program Sederhana dengan Fitur CRUD

# Data inventaris dalam bentuk list of dictionaries
inventory = [
    {
        "kode": "F001",
        "nama": "Lifebuoy Sabun Mandi",
        "kategori": "Pembersih",
        "stok": 100,
        "satuan": "rcg",
        "harga": 5000,
        "lokasi": "Rak A-1",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F002",
        "nama": "Dove Shampoo Daily Shine",
        "kategori": "Perawatan",
        "stok": 75,
        "satuan": "rcg",
        "harga": 25000,
        "lokasi": "Rak A-2",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F003",
        "nama": "Cakra Kembar Tepung Terigu",
        "kategori": "Bahan Makanan",
        "stok": 50,
        "satuan": "ctn",
        "harga": 12000,
        "lokasi": "Rak B-1",
        "supplier": "PT Bogasari"
    },
    {
        "kode": "F004",
        "nama": "Bimoli Minyak Goreng Premium",
        "kategori": "Bahan Makanan",
        "stok": 80,
        "satuan": "rcg",
        "harga": 20000,
        "lokasi": "Rak B-2",
        "supplier": "PT Bimoli"
    },
    {
        "kode": "F005",
        "nama": "Pepsodent Pasta Gigi Herbal",
        "kategori": "Perawatan",
        "stok": 120,
        "satuan": "rcg",
        "harga": 15000,
        "lokasi": "Rak A-3",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F006",
        "nama": "Rinso Deterjen Bubuk Premium",
        "kategori": "Pembersih",
        "stok": 60,
        "satuan": "ctn",
        "harga": 65000,
        "lokasi": "Rak A-4",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F007",
        "nama": "Sunlight Sabun Cuci Piring",
        "kategori": "Pembersih",
        "stok": 90,
        "satuan": "rcg",
        "harga": 12000,
        "lokasi": "Rak A-5",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F008",
        "nama": "Sariwangi Teh Celup Premium",
        "kategori": "Minuman",
        "stok": 150,
        "satuan": "ctn",
        "harga": 35000,
        "lokasi": "Rak C-1",
        "supplier": "PT Sariwangi"
    },
    {
        "kode": "F009",
        "nama": "Indomie Mi Goreng Special",
        "kategori": "Makanan Instan",
        "stok": 200,
        "satuan": "ctn",
        "harga": 50000,
        "lokasi": "Rak C-2",
        "supplier": "PT Indofood"
    },
    {
        "kode": "F010",
        "nama": "Royco Bumbu Masak Siap Pakai",
        "kategori": "Bumbu Masak",
        "stok": 70,
        "satuan": "rcg",
        "harga": 18000,
        "lokasi": "Rak C-3",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F011",
        "nama": "Blue Band Margarin Premium",
        "kategori": "Bahan Makanan",
        "stok": 45,
        "satuan": "rcg",
        "harga": 22000,
        "lokasi": "Rak B-3",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F012",
        "nama": "Sunsilk Shampoo Black Shine",
        "kategori": "Perawatan",
        "stok": 85,
        "satuan": "rcg",
        "harga": 23000,
        "lokasi": "Rak A-6",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F013",
        "nama": "Molto Pewangi Pakaian Premium",
        "kategori": "Pembersih",
        "stok": 110,
        "satuan": "rcg",
        "harga": 14000,
        "lokasi": "Rak A-7",
        "supplier": "PT Wings"
    },
    {
        "kode": "F014",
        "nama": "Sedaap Mi Goreng Special",
        "kategori": "Makanan Instan",
        "stok": 180,
        "satuan": "ctn",
        "harga": 45000,
        "lokasi": "Rak C-4",
        "supplier": "PT Wings"
    },
    {
        "kode": "F015",
        "nama": "Bango Kecap Manis Premium",
        "kategori": "Bumbu Masak",
        "stok": 95,
        "satuan": "rcg",
        "harga": 20000,
        "lokasi": "Rak C-5",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F016",
        "nama": "Rinso Deterjen Cair Premium",
        "kategori": "Pembersih",
        "stok": 65,
        "satuan": "rcg",
        "harga": 35000,
        "lokasi": "Rak A-8",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F017",
        "nama": "Sariwangi Teh Celup Jasmine",
        "kategori": "Minuman",
        "stok": 130,
        "satuan": "ctn",
        "harga": 40000,
        "lokasi": "Rak C-6",
        "supplier": "PT Sariwangi"
    },
    {
        "kode": "F018",
        "nama": "Palmia Minyak Goreng Premium",
        "kategori": "Bahan Makanan",
        "stok": 75,
        "satuan": "rcg",
        "harga": 22000,
        "lokasi": "Rak B-4",
        "supplier": "PT Salim Ivomas"
    },
    {
        "kode": "F019",
        "nama": "Close Up Pasta Gigi Fresh",
        "kategori": "Perawatan",
        "stok": 140,
        "satuan": "rcg",
        "harga": 16000,
        "lokasi": "Rak A-9",
        "supplier": "PT Unilever"
    },
    {
        "kode": "F020",
        "nama": "Sasa Tepung Bumbu Siap Pakai",
        "kategori": "Bumbu Masak",
        "stok": 85,
        "satuan": "rcg",
        "harga": 19000,
        "lokasi": "Rak C-7",
        "supplier": "PT Sasa Inti"
    }
]

# Fungsi untuk mencetak header tabel
def print_table_header():
    print("\n{:<10} {:<30} {:<15} {:<8} {:<8} {:<15} {:<15} {:<15}".format(
        "KODE", "NAMA BARANG", "KATEGORI", "STOK", "SATUAN", "HARGA", "LOKASI", "SUPPLIER"))
    print("-" * 125)

# Fungsi untuk mencetak baris tabel
def print_table_row(item):
    print("{:<10} {:<30} {:<15} {:<8} {:<8} {:<15,} {:<15} {:<15}".format(
        item["kode"],
        item["nama"],
        item["kategori"],
        item["stok"],
        item["satuan"],
        item["harga"],
        item["lokasi"],
        item["supplier"]))

# Fungsi untuk mencetak detail barang
def print_detail(item):
    print("\n" + "=" * 50)
    print(f"Detail Barang: {item['nama']}")
    print("=" * 50)
    print(f"Kode Barang      : {item['kode']}")
    print(f"Nama Barang      : {item['nama']}")
    print(f"Kategori         : {item['kategori']}")
    print(f"Stok             : {item['stok']} {item['satuan']}")
    print(f"Harga            : Rp {item['harga']:,}")
    print(f"Lokasi           : {item['lokasi']}")
    print(f"Supplier         : {item['supplier']}")
    print("=" * 50)

# Fungsi untuk mencari barang berdasarkan kode
def find_item_by_code(code):
    for item in inventory:
        if item["kode"] == code:
            return item
    return None

# Fungsi untuk mengecek apakah kode sudah ada
def is_code_exists(code):
    return find_item_by_code(code) is not None

# Fungsi untuk mendapatkan daftar kategori yang ada
def get_categories():
    categories = []
    for item in inventory:
        if item["kategori"] not in categories:
            categories.append(item["kategori"])
    return categories

# Fungsi untuk validasi input angka
def validate_number(input_str):
    try:
        num = float(input_str)
        return num >= 0
    except ValueError:
        return False

# Fungsi untuk validasi kode format Fxxx tanpa library re
def validate_code_format(code):
    if len(code) != 4:
        return False
    if code[0] != 'F':
        return False
    for i in range(1, 4):
        if not code[i].isdigit():
            return False
    return True

# Fungsi untuk validasi format rak tanpa library re
def validate_rack_format(rack):
    # Format yang valid: "Rak X-Y" dimana X adalah huruf kapital dan Y adalah angka
    parts = rack.split()
    if len(parts) != 2 or parts[0] != "Rak":
        return False
    
    loc_parts = parts[1].split('-')
    if len(loc_parts) != 2:
        return False
    
    if not (len(loc_parts[0]) == 1 and loc_parts[0].isalpha() and loc_parts[0].isupper()):
        return False
    
    if not loc_parts[1].isdigit():
        return False
    
    return True

# ============== MENU UTAMA ==============
def main_menu():
    while True:
        print("\n" + "=" * 40)
        print("     SISTEM MANAJEMEN STOK BARANG FMCG")
        print("=" * 40)
        print("[1] Lihat Data Barang")
        print("[2] Tambah Barang Baru")
        print("[3] Update Data Barang")
        print("[4] Hapus Data Barang")
        print("[0] Keluar Program")
        print("-" * 40)
        
        choice = input("Pilih menu (0-4): ")
        
        if choice == "1":
            read_menu()
        elif choice == "2":
            create_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "0":
            confirm = input("Apakah Anda yakin ingin keluar? (y/n): ").lower()
            if confirm == 'y':
                print("\nTerima kasih telah menggunakan Sistem Manajemen Stok Barang FMCG!")
                break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

# ============== READ MENU ==============
def read_menu():
    while True:
        print("\n" + "=" * 40)
        print("       LIHAT DATA BARANG")
        print("=" * 40)
        print("[1] Lihat Semua Barang")
        print("[2] Lihat Barang Berdasarkan Kategori")
        print("[3] Cari Barang Berdasarkan Kode")
        print("[0] Kembali ke Menu Utama")
        print("-" * 40)
        
        choice = input("Pilih menu (0-3): ")
        
        if choice == "1":
            # Lihat semua barang
            if not inventory:
                print("\nTidak ada data barang.")
            else:
                print("\n" + "=" * 40)
                print("        DAFTAR SEMUA BARANG")
                print("=" * 40)
                
                print_table_header()
                for item in inventory:
                    print_table_row(item)
            
            input("\nTekan Enter untuk kembali...")
        elif choice == "2":
            # Lihat berdasarkan kategori
            categories = get_categories()
            
            if not categories:
                print("\nTidak ada kategori tersedia.")
            else:
                print("\nKategori yang tersedia:")
                for i, category in enumerate(categories, 1):
                    print(f"[{i}] {category}")
                print("[0] Kembali ke Menu Sebelumnya")
                
                cat_choice = input(f"\nPilih kategori (0-{len(categories)}): ")
                
                if cat_choice == "0":
                    continue
                
                if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
                    selected_category = categories[int(cat_choice) - 1]
                    
                    # Filter barang berdasarkan kategori
                    filtered_items = [item for item in inventory if item["kategori"] == selected_category]
                    
                    if not filtered_items:
                        print(f"\nTidak ada barang dalam kategori {selected_category}.")
                    else:
                        print(f"\n" + "=" * 40)
                        print(f"    DAFTAR BARANG KATEGORI: {selected_category}")
                        print("=" * 40)
                        
                        print_table_header()
                        for item in filtered_items:
                            print_table_row(item)
                else:
                    print("\nPilihan kategori tidak valid.")
            
            input("\nTekan Enter untuk kembali...")
        elif choice == "3":
            # Cari berdasarkan kode
            kode = input("\nMasukkan kode barang - Tekan 0 untuk batal: ").upper()
            
            if kode == "0":
                continue
                
            item = find_item_by_code(kode)
            
            if item:
                print_detail(item)
            else:
                print("\nBarang dengan kode tersebut tidak ditemukan.")
            
            input("\nTekan Enter untuk kembali...")
        elif choice == "0":
            # Kembali ke menu utama
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

# ============== CREATE ITEM ==============
def create_item():
    print("\n" + "=" * 40)
    print("        TAMBAH BARANG BARU")
    print("=" * 40)
    print("-" * 40)
    
    # Input dan validasi kode barang
    print("Tekan 0 untuk batal . . .")
    while True:
        kode = input("Kode Barang (format: Fxxx): ").upper()
        if kode == "0":
            print("\nKembali ke menu utama...")
            return
        if not kode:
            print("Kode barang tidak boleh kosong!")
            continue
        if is_code_exists(kode):
            print("Kode barang sudah ada dalam sistem!")
            continue
        if not validate_code_format(kode):
            print("Format kode barang tidak valid! Gunakan format Fxxx (F diikuti 3 digit angka)")
            continue
        break
    
    # Input nama barang
    print("\nTekan 0 untuk batal")
    while True:
        nama = input("Nama Barang: ")
        if nama == "0":
            print("\nKembali ke menu utama...")
            return
        if not nama:
            print("Nama barang tidak boleh kosong!")
            continue
        break
    
    # Input kategori
    print("\nKategori yang tersedia:")
    categories = get_categories()
    for i, category in enumerate(categories, 1):
        print(f"[{i}] {category}")
    print(f"[{len(categories) + 1}] Tambah kategori baru")
    print("Tekan 0 untuk batal")
    
    while True:
        cat_choice = input(f"Pilih kategori (0-{len(categories) + 1}): ")
        if cat_choice == "0":
            print("\nKembali ke menu utama...")
            return
        
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            kategori = categories[int(cat_choice) - 1]
            break
        elif cat_choice.isdigit() and int(cat_choice) == len(categories) + 1:
            print("\nTekan 0 untuk batal")
            while True:
                kategori = input("Masukkan kategori baru: ")
                if kategori == "0":
                    print("\nKembali ke menu utama...")
                    return
                if kategori:
                    break
                print("Kategori tidak boleh kosong!")
            break
        else:
            print("Pilihan tidak valid!")
    
    # Input stok
    print("\nTekan 0 untuk batal")
    while True:
        stok_str = input("Stok Barang: ")
        if stok_str == "0":
            print("\nKembali ke menu utama...")
            return
        if stok_str.isdigit() and int(stok_str) >= 0:
            stok = int(stok_str)
            break
        print("Stok harus berupa angka positif!")
    
    # Input satuan
    print("\nPilih satuan:")
    print("[1] rcg (Renceng)")
    print("[2] ctn (Karton)")
    print("Tekan 0 untuk batal")
    
    while True:
        satuan_choice = input("Pilihan (0-2): ")
        if satuan_choice == "0":
            print("\nKembali ke menu utama...")
            return
        if satuan_choice in ["1", "2"]:
            satuan = "rcg" if satuan_choice == "1" else "ctn"
            break
        print("Pilihan tidak valid!")
    
    # Input harga
    print("\nTekan 0 untuk batal")
    while True:
        harga_str = input("Harga Barang (Rp): ")
        if harga_str == "0":
            print("\nKembali ke menu utama...")
            return
        if validate_number(harga_str):
            harga = float(harga_str)
            break
        print("Harga harus berupa angka positif!")
    
    # Input dan validasi lokasi rak
    print("\nTekan 0 untuk batal")
    while True:
        lokasi = input("Lokasi Penyimpanan (format: Rak X-Y): ")
        if lokasi == "0":
            print("\nKembali ke menu utama...")
            return
        if not lokasi:
            print("Lokasi tidak boleh kosong!")
            continue
        if not validate_rack_format(lokasi):
            print("Format lokasi tidak valid! Gunakan format Rak X-Y (contoh: Rak A-1)")
            continue
        break
    
    # Input supplier
    print("\nTekan 0 untuk batal")
    while True:
        supplier = input("Supplier: ")
        if supplier == "0":
            print("\nKembali ke menu utama...")
            return
        if not supplier:
            print("Supplier tidak boleh kosong!")
            continue
        break
    
    # Konfirmasi data
    print("\nDetail barang yang akan ditambahkan:")
    new_item = {
        "kode": kode,
        "nama": nama,
        "kategori": kategori,
        "stok": stok,
        "satuan": satuan,
        "harga": harga,
        "lokasi": lokasi,
        "supplier": supplier
    }
    
    print_detail(new_item)
    
    print("\n[y] Ya")
    print("[n] Tidak")
    print("[0] Kembali ke Menu Utama")
    confirm = input("Apakah data sudah benar? (y/n/0): ").lower()
    if confirm == "0":
        print("\nKembali ke menu utama...")
        return
    elif confirm == 'y':
        inventory.append(new_item)
        print(f"\nBarang {nama} berhasil ditambahkan!")
    else:
        print("\nPenambahan barang dibatalkan.")
    
    input("\nTekan Enter untuk kembali ke menu utama...")

# ============== UPDATE ITEM ==============
def update_item():
    print("\n" + "=" * 40)
    print("        UPDATE DATA BARANG")
    print("=" * 40)
    print("-" * 40)
    
    print("Tekan 0 untuk batal")
    kode = input("Masukkan kode barang: ").upper()
    if kode == "0":
        print("\nKembali ke menu utama...")
        return
        
    item = find_item_by_code(kode)
    
    if not item:
        print("\nBarang dengan kode tersebut tidak ditemukan!")
        input("\nTekan Enter untuk kembali ke menu utama...")
        return
    
    print("\nDetail barang:")
    print_detail(item)
    
    print("\nPilih data yang akan diupdate:")
    print("[1] Nama")
    print("[2] Kategori")
    print("[3] Stok")
    print("[4] Satuan")
    print("[5] Harga")
    print("[6] Lokasi")
    print("[7] Supplier")
    print("[0] Kembali ke Menu Utama")
    
    choice = input("\nPilihan (0-7): ")
    
    if choice == "1":
        print("\nTekan 0 untuk batal")
        nama = input("Masukkan nama baru: ")
        if nama == "0":
            print("\nUpdate dibatalkan.")
            return
        if nama:
            item['nama'] = nama
            print(f"\nNama barang berhasil diupdate menjadi {nama}")
        else:
            print("\nNama tidak boleh kosong!")
    elif choice == "2":
        print("\nKategori yang tersedia:")
        categories = get_categories()
        for i, category in enumerate(categories, 1):
            print(f"[{i}] {category}")
        print(f"[{len(categories) + 1}] Tambah kategori baru")
        print("[0] Kembali ke Menu Utama")
        
        cat_choice = input(f"Pilih kategori (0-{len(categories) + 1}): ")
        if cat_choice == "0":
            print("\nUpdate dibatalkan.")
            return
            
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            item['kategori'] = categories[int(cat_choice) - 1]
            print(f"\nKategori barang berhasil diupdate menjadi {item['kategori']}")
        elif cat_choice.isdigit() and int(cat_choice) == len(categories) + 1:
            print("\nTekan 0 untuk batal")
            kategori = input("Masukkan kategori baru: ")
            if kategori == "0":
                print("\nUpdate dibatalkan.")
                return
            if kategori:
                item['kategori'] = kategori
                print(f"\nKategori barang berhasil diupdate menjadi {kategori}")
            else:
                print("\nKategori tidak boleh kosong!")
        else:
            print("\nPilihan tidak valid!")
    elif choice == "3":
        print("\nTekan 0 untuk batal")
        stok_str = input("Masukkan jumlah stok baru: ")
        if stok_str == "0":
            print("\nUpdate dibatalkan.")
            return
        if stok_str.isdigit() and int(stok_str) >= 0:
            item['stok'] = int(stok_str)
            print(f"\nStok barang berhasil diupdate menjadi {item['stok']}")
        else:
            print("\nStok harus berupa angka positif!")
    elif choice == "4":
        print("\nPilih satuan:")
        print("[1] rcg (Renceng)")
        print("[2] ctn (Karton)")
        print("[0] Kembali ke Menu Utama")
        
        satuan_choice = input("Pilihan (0-2): ")
        if satuan_choice == "0":
            print("\nUpdate dibatalkan.")
            return
        if satuan_choice in ["1", "2"]:
            item['satuan'] = "rcg" if satuan_choice == "1" else "ctn"
            print(f"\nSatuan barang berhasil diupdate menjadi {item['satuan']}")
        else:
            print("\nPilihan tidak valid!")
    elif choice == "5":
        print("\nTekan 0 untuk batal")
        harga_str = input("Masukkan harga baru: ")
        if harga_str == "0":
            print("\nUpdate dibatalkan.")
            return
        if validate_number(harga_str):
            item['harga'] = float(harga_str)
            print(f"\nHarga barang berhasil diupdate menjadi Rp {item['harga']:,}")
        else:
            print("\nHarga harus berupa angka positif!")
    elif choice == "6":
        print("\nTekan 0 untuk batal")
        while True:
            lokasi = input("Masukkan lokasi baru (format: Rak X-Y): ")
            if lokasi == "0":
                print("\nUpdate dibatalkan.")
                return
            if not lokasi:
                print("\nLokasi tidak boleh kosong!")
                continue
            if not validate_rack_format(lokasi):
                print("\nFormat lokasi tidak valid! Gunakan format Rak X-Y (contoh: Rak A-1)")
                continue
            item['lokasi'] = lokasi
            print(f"\nLokasi barang berhasil diupdate menjadi {lokasi}")
            break
    elif choice == "7":
        print("\nTekan 0 untuk batal")
        supplier = input("Masukkan supplier baru: ")
        if supplier == "0":
            print("\nUpdate dibatalkan.")
            return
        if supplier:
            item['supplier'] = supplier
            print(f"\nSupplier barang berhasil diupdate menjadi {supplier}")
        else:
            print("\nSupplier tidak boleh kosong!")
    elif choice == "0":
        print("\nUpdate dibatalkan.")
    else:
        print("\nPilihan tidak valid!")
    
    input("\nTekan Enter untuk kembali ke menu utama...")

# ============== DELETE ITEM ==============
def delete_item():
    print("\n" + "=" * 40)
    print("        HAPUS DATA BARANG")
    print("=" * 40)
    print("-" * 40)
    
    print("Tekan 0 untuk batal")
    kode = input("Masukkan kode barang yang akan dihapus: ").upper()
    if kode == "0":
        print("\nKembali ke menu utama...")
        return
        
    item = find_item_by_code(kode)
    
    if not item:
        print("\nBarang dengan kode tersebut tidak ditemukan!")
        input("\nTekan Enter untuk kembali ke menu utama...")
        return
    
    print("\nDetail barang yang akan dihapus:")
    print_detail(item)
    
    print("\n[y] Ya")
    print("[n] Tidak")
    print("[0] Kembali ke Menu Utama")
    confirm = input("Apakah Anda yakin ingin menghapus barang ini? (y/n/0): ").lower()
    if confirm == "0":
        print("\nKembali ke menu utama...")
        return
    elif confirm == 'y':
        inventory.remove(item)
        print(f"\nBarang {item['nama']} berhasil dihapus!")
    else:
        print("\nPenghapusan barang dibatalkan.")
    
    input("\nTekan Enter untuk kembali ke menu utama...")

# ============== MAIN PROGRAM ==============
if __name__ == "__main__":
    main_menu()