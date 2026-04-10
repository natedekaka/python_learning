#!/usr/bin/env python3
"""
Advanced - Exercise 1: Object-Oriented Programming
==================================================

SOAL:
1. Buat class Siswa dengan attributes dan methods
2. Buat class dengan constructor (__init__)
3. Buat methods untuk menampilkan data
4. Implementasi multiple objects
5. Buat class inheritance
"""

# ===== SOAL 1 & 2: Class Definition =====
print("=" * 50)
print("SOAL 1 & 2: Class Siswa")
print("=" * 50)

class Siswa:
    """Class untuk merepresentasikan seorang siswa"""
    
    # Class variable (shared by all instances)
    sekolah = "SMA Negeri 1"
    total_siswa = 0
    
    # Constructor
    def __init__(self, nama, umur, nilai):
        """Initialize siswa dengan nama, umur, dan nilai"""
        self.nama = nama
        self.umur = umur
        self.nilai = nilai
        Siswa.total_siswa += 1
    
    # Methods
    def tampilkan_info(self):
        """Tampilkan informasi siswa"""
        return f"Nama: {self.nama}, Umur: {self.umur}, Nilai: {self.nilai}"
    
    def tambah_nilai(self, tambahan):
        """Tambah nilai siswa"""
        self.nilai += tambahan
        return f"Nilai {self.nama} ditambah {tambahan} menjadi {self.nilai}"
    
    def dapatkan_grade(self):
        """Dapatkan grade berdasarkan nilai"""
        if self.nilai >= 90:
            return "A"
        elif self.nilai >= 80:
            return "B"
        elif self.nilai >= 70:
            return "C"
        else:
            return "D"
    
    def __str__(self):
        """String representation"""
        return f"{self.nama} (Grade: {self.dapatkan_grade()})"

# ===== SOAL 4: Buat Objects =====
print("\n" + "=" * 50)
print("SOAL 4: Create Multiple Objects")
print("=" * 50)

siswa1 = Siswa("Ari", 16, 85)
siswa2 = Siswa("Budi", 16, 92)
siswa3 = Siswa("Citra", 17, 78)

print(f"Siswa 1: {siswa1.tampilkan_info()}")
print(f"Siswa 2: {siswa2.tampilkan_info()}")
print(f"Siswa 3: {siswa3.tampilkan_info()}")

print(f"\nTotal siswa: {Siswa.total_siswa}")
print(f"Sekolah: {Siswa.sekolah}")

# ===== SOAL 3: Display Methods =====
print("\n" + "=" * 50)
print("SOAL 3: Methods & Operations")
print("=" * 50)

print(f"\nGrade {siswa1.nama}: {siswa1.dapatkan_grade()}")
print(f"Grade {siswa2.nama}: {siswa2.dapatkan_grade()}")
print(f"Grade {siswa3.nama}: {siswa3.dapatkan_grade()}")

print(f"\n{siswa1.tambah_nilai(5)}")
print(f"Info updated: {siswa1.tampilkan_info()}")

# ===== SOAL 5: Inheritance =====
print("\n" + "=" * 50)
print("SOAL 5: Class Inheritance")
print("=" * 50)

class SiswaBerprestasi(Siswa):
    """Class turunan dari Siswa untuk siswa berprestasi"""
    
    def __init__(self, nama, umur, nilai, prestasi):
        """Initialize dengan tambahan prestasi"""
        super().__init__(nama, umur, nilai)
        self.prestasi = prestasi
    
    def tampilkan_info(self):
        """Override method dari parent class"""
        info_parent = super().tampilkan_info()
        return f"{info_parent}, Prestasi: {self.prestasi}"
    
    def bonus_nilai(self):
        """Bonus nilai untuk siswa berprestasi"""
        self.nilai += 10
        return f"Bonus 10 poin untuk {self.prestasi}"

siswa_juara = SiswaBerprestasi("Doni", 16, 88, "Juara Olimpiade Matematika")
print(f"\nSiswa Berprestasi: {siswa_juara.tampilkan_info()}")
print(f"{siswa_juara.bonus_nilai()}")
print(f"Info setelah bonus: {siswa_juara.tampilkan_info()}")

# ===== Polymorphism =====
print("\n" + "=" * 50)
print("SOAL BONUS: Polymorphism")
print("=" * 50)

siswa_list = [siswa1, siswa2, siswa3, siswa_juara]

print("Daftar semua siswa:")
for siswa in siswa_list:
    print(f"  - {siswa}")

print("\n✅ Latihan Selesai!")
