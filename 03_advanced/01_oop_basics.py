#!/usr/bin/env python3
"""
Phase 5: Object-Oriented Programming (OOP)
===========================================
Belajar: class, object, method, inheritance, polymorphism
"""

print("=" * 50)
print("PHASE 5: OBJECT-ORIENTED PROGRAMMING (OOP)")
print("=" * 50)

# ===== 1. BASIC CLASS & OBJECT =====
print("\n=== 1. BASIC CLASS & OBJECT ===\n")

class Siswa:
    """Kelas untuk merepresentasikan seorang siswa"""
    
    # Constructor (__init__)
    def __init__(self, nama, umur, nilai):
        self.nama = nama
        self.umur = umur
        self.nilai = nilai
    
    # Method (fungsi dalam class)
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self.umur}, Nilai: {self.nilai}")
    
    def hitung_grade(self):
        if self.nilai >= 90:
            return "A"
        elif self.nilai >= 80:
            return "B"
        elif self.nilai >= 70:
            return "C"
        else:
            return "D"

# Membuat object (instance)
siswa1 = Siswa("Ari", 25, 85)
siswa2 = Siswa("Budi", 26, 92)

# Akses method
siswa1.tampilkan_info()
print(f"Grade: {siswa1.hitung_grade()}\n")

siswa2.tampilkan_info()
print(f"Grade: {siswa2.hitung_grade()}\n")

# ===== 2. CLASS VARIABLES VS INSTANCE VARIABLES =====
print("=== 2. CLASS VARIABLES VS INSTANCE VARIABLES ===\n")

class Kelas:
    """Kelas untuk sekolah"""
    total_siswa = 0  # Class variable (shared)
    
    def __init__(self, nama_kelas):
        self.nama_kelas = nama_kelas  # Instance variable
        Kelas.total_siswa += 1
    
    def info(self):
        print(f"Kelas: {self.nama_kelas}")

kelas1 = Kelas("X IPA 1")
kelas2 = Kelas("X IPA 2")
kelas3 = Kelas("X IPS 1")

print(f"Total kelas dibuat: {Kelas.total_siswa}")

# ===== 3. SPECIAL METHODS (__str__, __repr__) =====
print("\n=== 3. SPECIAL METHODS ===\n")

class Mobil:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def __str__(self):
        """Dipanggil saat print() atau str()"""
        return f"Mobil {self.merek} tahun {self.tahun}"
    
    def __repr__(self):
        """Representasi untuk debugging"""
        return f"Mobil('{self.merek}', {self.tahun})"
    
    def __len__(self):
        """Dijalankan saat len()"""
        return self.tahun

mobil1 = Mobil("Toyota", 2020)
print(mobil1)  # Gunakan __str__
print(repr(mobil1))  # Gunakan __repr__
print(f"Tahun: {len(mobil1)}\n")

# ===== 4. INHERITANCE (Pewarisan) =====
print("=== 4. INHERITANCE (Pewarisan) ===\n")

class Kendaraan:
    """Parent class"""
    def __init__(self, merek):
        self.merek = merek
    
    def info(self):
        print(f"Merek: {self.merek}")

class Mobil(Kendaraan):
    """Child class (inherit dari Kendaraan)"""
    def __init__(self, merek, roda):
        super().__init__(merek)  # Panggil parent __init__
        self.roda = roda
    
    def info(self):
        super().info()  # Panggil parent method
        print(f"Roda: {self.roda}")

class Motor(Kendaraan):
    """Child class lain"""
    def __init__(self, merek, roda):
        super().__init__(merek)
        self.roda = roda
    
    def info(self):
        super().info()
        print(f"Roda: {self.roda}")

mobil = Mobil("Honda", 4)
motor = Motor("Yamaha", 2)

print("Mobil:")
mobil.info()

print("\nMotor:")
motor.info()

# ===== 5. POLYMORPHISM (Polimorfisme) =====
print("\n=== 5. POLYMORPHISM (Polimorfisme) ===\n")

class Hewan:
    def bersuara(self):
        pass

class Anjing(Hewan):
    def bersuara(self):
        print("Guk guk!")

class Kucing(Hewan):
    def bersuara(self):
        print("Meow meow!")

class Sapi(Hewan):
    def bersuara(self):
        print("Mooo!")

# Polymorphism: method yang sama, behavior berbeda
hewan_list = [Anjing(), Kucing(), Sapi()]

print("Suara hewan:")
for hewan in hewan_list:
    hewan.bersuara()

# ===== 6. ENCAPSULATION (Pembungkusan) =====
print("\n=== 6. ENCAPSULATION (Pembungkusan) ===\n")

class BankAccount:
    def __init__(self, pemilik, saldo_awal=0):
        self.pemilik = pemilik
        self.__saldo = saldo_awal  # Private variable (__)
    
    # Getter
    def get_saldo(self):
        return self.__saldo
    
    # Setter
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor {jumlah} berhasil. Saldo: {self.__saldo}")
        else:
            print("Jumlah harus positif!")
    
    def tarik(self, jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Tarik {jumlah} berhasil. Saldo: {self.__saldo}")
        else:
            print("Jumlah invalid atau saldo tidak cukup!")

akun = BankAccount("Ari", 100000)
print(f"Pemilik: {akun.pemilik}, Saldo: {akun.get_saldo()}")
akun.setor(50000)
akun.tarik(30000)
akun.tarik(200000)  # Akan error

# ===== 7. CLASS METHODS & STATIC METHODS =====
print("\n=== 7. CLASS METHODS & STATIC METHODS ===\n")

class Lingkaran:
    PI = 3.14
    total_dibuat = 0
    
    def __init__(self, radius):
        self.radius = radius
        Lingkaran.total_dibuat += 1
    
    def luas(self):
        return Lingkaran.PI * self.radius ** 2
    
    @classmethod
    def dari_diameter(cls, diameter):
        """Class method: membuat instance dari diameter"""
        return cls(diameter / 2)
    
    @staticmethod
    def is_valid_radius(radius):
        """Static method: tidak perlu self atau cls"""
        return radius > 0

# Membuat lingkaran
lingkaran1 = Lingkaran(5)
print(f"Lingkaran radius 5, luas: {lingkaran1.luas():.2f}")

# Menggunakan class method
lingkaran2 = Lingkaran.dari_diameter(14)
print(f"Lingkaran dari diameter 14, luas: {lingkaran2.luas():.2f}")

# Menggunakan static method
print(f"Radius 5 valid? {Lingkaran.is_valid_radius(5)}")
print(f"Radius -5 valid? {Lingkaran.is_valid_radius(-5)}")
print(f"Total lingkaran dibuat: {Lingkaran.total_dibuat}\n")

# ===== 8. ABSTRACT CLASS & INHERITANCE =====
print("=== 8. MULTIPLE INHERITANCE ===\n")

class Mamalia:
    def bergerak(self):
        return "Berjalan"

class Penerbang:
    def bergerak(self):
        return "Terbang"

class Kelelawar(Mamalia, Penerbang):
    pass

kelelawar = Kelelawar()
print(f"Kelelawar bergerak dengan: {kelelawar.bergerak()}")

# ===== 9. PROPERTY DECORATOR =====
print("\n=== 9. PROPERTY DECORATOR ===\n")

class Celcius:
    def __init__(self, nilai):
        self._celcius = nilai
    
    @property
    def celsius(self):
        """Getter"""
        return self._celcius
    
    @property
    def fahrenheit(self):
        """Hitung Fahrenheit dari Celsius"""
        return (self._celcius * 9/5) + 32
    
    @celsius.setter
    def celsius(self, nilai):
        """Setter"""
        if nilai < -273.15:
            raise ValueError("Suhu tidak bisa kurang dari -273.15°C")
        self._celcius = nilai

temp = Celcius(0)
print(f"0°C = {temp.fahrenheit:.2f}°F")

temp.celsius = 25
print(f"{temp.celsius}°C = {temp.fahrenheit:.2f}°F")

# ===== 10. COMPOSITION (Komposisi) =====
print("\n=== 10. COMPOSITION (Komposisi) ===\n")

class Mesin:
    def __init__(self, tipe):
        self.tipe = tipe
    
    def nyalakan(self):
        print(f"Mesin {self.tipe} menyala")

class Mobil2:
    def __init__(self, merek, mesin_tipe):
        self.merek = merek
        self.mesin = Mesin(mesin_tipe)  # Composition
    
    def mulai(self):
        print(f"Mobil {self.merek} dimulai")
        self.mesin.nyalakan()

mobil = Mobil2("Toyota", "Bensin 2.0L")
mobil.mulai()

# ===== 11. PRACTICAL EXAMPLE =====
print("\n=== 11. PRACTICAL EXAMPLE: SISTEM NILAI SEKOLAH ===\n")

class Guru:
    def __init__(self, nama, mata_pelajaran):
        self.nama = nama
        self.mata_pelajaran = mata_pelajaran
    
    def __str__(self):
        return f"Guru {self.nama} (Mapel: {self.mata_pelajaran})"

class Pelajaran:
    def __init__(self, nama, guru):
        self.nama = nama
        self.guru = guru
        self.daftar_nilai = {}
    
    def tambah_nilai(self, nama_siswa, nilai):
        self.daftar_nilai[nama_siswa] = nilai
    
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        return sum(self.daftar_nilai.values()) / len(self.daftar_nilai)
    
    def laporan(self):
        print(f"\nPelajaran: {self.nama}")
        print(f"Guru: {self.guru.nama}")
        print("Nilai siswa:")
        for siswa, nilai in self.daftar_nilai.items():
            print(f"  {siswa}: {nilai}")
        print(f"Rata-rata: {self.rata_rata():.2f}")

guru_mtk = Guru("Bu Siti", "Matematika")
mtk = Pelajaran("Matematika", guru_mtk)

mtk.tambah_nilai("Ari", 85)
mtk.tambah_nilai("Budi", 92)
mtk.tambah_nilai("Citra", 78)

mtk.laporan()

print("\n" + "=" * 50)
print("SELESAI FASE 5!")
print("=" * 50)
