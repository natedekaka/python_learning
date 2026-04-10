#!/usr/bin/env python3
"""
OOP Practice Exercise
=====================
Buat sistem manajemen perpustakaan

TODO:
1. Buat class Buku dengan attributes: judul, pengarang, tahun, tersedia
2. Buat class Anggota dengan attributes: nama, id, buku_pinjam (list)
3. Buat method: pinjam_buku(), kembalikan_buku()
4. Buat class Perpustakaan untuk manage buku dan anggota
"""

print("=" * 50)
print("LATIHAN OOP: SISTEM MANAJEMEN PERPUSTAKAAN")
print("=" * 50)

# ===== 1. CLASS BUKU =====
print("\n=== 1. CLASS BUKU ===\n")

class Buku:
    """Class untuk merepresentasikan sebuah buku"""
    
    def __init__(self, judul, pengarang, tahun):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun = tahun
        self.tersedia = True
    
    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"'{self.judul}' oleh {self.pengarang} ({self.tahun}) - {status}"
    
    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False
    
    def kembalikan(self):
        self.tersedia = True

# Test class Buku
buku1 = Buku("Python 101", "Guido van Rossum", 2020)
buku2 = Buku("Clean Code", "Robert Martin", 2008)
buku3 = Buku("The Pragmatic Programmer", "Hunt & Thomas", 1999)

print(f"Buku 1: {buku1}")
print(f"Buku 2: {buku2}")
print(f"Buku 3: {buku3}\n")

# ===== 2. CLASS ANGGOTA =====
print("=== 2. CLASS ANGGOTA ===\n")

class Anggota:
    """Class untuk merepresentasikan anggota perpustakaan"""
    
    id_counter = 1000  # Class variable untuk auto increment
    
    def __init__(self, nama):
        self.nama = nama
        self.id = Anggota.id_counter
        Anggota.id_counter += 1
        self.buku_pinjam = []
    
    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.buku_pinjam.append(buku)
            print(f"✓ {self.nama} meminjam: {buku.judul}")
            return True
        else:
            print(f"✗ {buku.judul} tidak tersedia!")
            return False
    
    def kembalikan_buku(self, buku):
        if buku in self.buku_pinjam:
            self.buku_pinjam.remove(buku)
            buku.kembalikan()
            print(f"✓ {self.nama} mengembalikan: {buku.judul}")
            return True
        else:
            print(f"✗ {self.nama} tidak meminjam buku ini!")
            return False
    
    def tampilkan_info(self):
        print(f"\nAnggota: {self.nama} (ID: {self.id})")
        if self.buku_pinjam:
            print(f"Buku yang dipinjam ({len(self.buku_pinjam)}):")
            for buku in self.buku_pinjam:
                print(f"  - {buku.judul}")
        else:
            print("Tidak ada buku yang dipinjam")

# Test class Anggota
anggota1 = Anggota("Ari")
anggota2 = Anggota("Budi")

anggota1.tampilkan_info()
anggota2.tampilkan_info()

# ===== 3. PINJAM BUKU =====
print("\n=== 3. PINJAM BUKU ===\n")

anggota1.pinjam_buku(buku1)
anggota1.pinjam_buku(buku2)
anggota2.pinjam_buku(buku1)  # Akan gagal karena sudah dipinjam

print(f"\nStatus buku setelah dipinjam:")
print(f"  {buku1}")
print(f"  {buku2}")

# ===== 4. TAMPILKAN INFO ANGGOTA =====
print("\n=== 4. INFO ANGGOTA SETELAH PINJAM ===\n")

anggota1.tampilkan_info()
anggota2.tampilkan_info()

# ===== 5. KEMBALIKAN BUKU =====
print("\n=== 5. KEMBALIKAN BUKU ===\n")

anggota1.kembalikan_buku(buku1)
anggota2.pinjam_buku(buku1)  # Sekarang bisa karena sudah dikembalikan

print(f"\nStatus buku setelah dikembalikan:")
print(f"  {buku1}")

# ===== 6. CLASS PERPUSTAKAAN =====
print("\n=== 6. CLASS PERPUSTAKAAN ===\n")

class Perpustakaan:
    """Class untuk mengelola perpustakaan"""
    
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []
        self.daftar_anggota = []
    
    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"✓ Buku ditambahkan: {buku.judul}")
    
    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)
        print(f"✓ Anggota ditambahkan: {anggota.nama}")
    
    def hitung_buku_tersedia(self):
        return sum(1 for buku in self.daftar_buku if buku.tersedia)
    
    def hitung_buku_dipinjam(self):
        return len(self.daftar_buku) - self.hitung_buku_tersedia()
    
    def laporan(self):
        print(f"\n{'=' * 50}")
        print(f"LAPORAN PERPUSTAKAAN: {self.nama}")
        print(f"{'=' * 50}")
        
        print(f"\nTotal buku: {len(self.daftar_buku)}")
        print(f"  - Tersedia: {self.hitung_buku_tersedia()}")
        print(f"  - Dipinjam: {self.hitung_buku_dipinjam()}")
        
        print(f"\nDaftar buku di perpustakaan:")
        for buku in self.daftar_buku:
            print(f"  {buku}")
        
        print(f"\nTotal anggota: {len(self.daftar_anggota)}")
        for anggota in self.daftar_anggota:
            anggota.tampilkan_info()

# Test class Perpustakaan
perpus = Perpustakaan("Perpustakaan Kota")

# Tambah buku
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)
perpus.tambah_buku(buku3)

# Tambah anggota
perpus.tambah_anggota(anggota1)
perpus.tambah_anggota(anggota2)

# Tampilkan laporan
perpus.laporan()

print("\n" + "=" * 50)
print("SELESAI LATIHAN OOP!")
print("=" * 50)

# ===== CHALLENGE (OPSIONAL) =====
"""
Challenge:
1. Tambahkan denda untuk anggota yang terlambat
   - Setiap buku yang dipinjam max 7 hari
   - Denda: 5000 per hari keterlambatan
   
2. Tambahkan method untuk pencarian buku:
   - Cari berdasarkan judul
   - Cari berdasarkan pengarang
   - Cari berdasarkan tahun
   
3. Tambahkan statistik:
   - Buku yang paling banyak dipinjam
   - Anggota yang paling aktif
   - Riwayat peminjaman
"""
