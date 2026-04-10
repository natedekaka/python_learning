#!/usr/bin/env python3
"""
PROJECT: Sistem Manajemen Siswa SMAN 6 Cimahi
Deskripsi: Program untuk mengelola data siswa, guru, dan nilai
Sekolah: SMAN Negeri 6 Cimahi
Program: Informatika
"""

class ManajemenSiswaClass:
    """Class untuk mengelola data siswa SMAN 6 Cimahi"""
    
    def __init__(self, nama_sekolah="SMAN Negeri 6 Cimahi"):
        self.nama_sekolah = nama_sekolah
        self.daftar_siswa = {}
    
    def tambah_siswa(self, nisn, nama, kelas):
        """Tambah siswa ke database SMAN 6"""
        if nisn not in self.daftar_siswa:
            self.daftar_siswa[nisn] = {
                "nama": nama,
                "kelas": kelas,
                "nilai": []
            }
            return True
        return False
    
    def cari_siswa(self, nisn):
        """Cari siswa SMAN 6 berdasarkan NISN"""
        return self.daftar_siswa.get(nisn)
    
    def tambah_nilai(self, nisn, nilai):
        """Tambah nilai siswa SMAN 6"""
        if nisn in self.daftar_siswa:
            self.daftar_siswa[nisn]["nilai"].append(nilai)
            return True
        return False
    
    def hitung_rata_rata(self, nisn):
        """Hitung rata-rata nilai siswa"""
        siswa = self.daftar_siswa.get(nisn)
        if siswa and siswa["nilai"]:
            return sum(siswa["nilai"]) / len(siswa["nilai"])
        return 0

# Contoh penggunaan
print("=" * 60)
print("SISTEM MANAJEMEN SISWA SMAN NEGERI 6 CIMAHI")
print("=" * 60)

sistem = ManajemenSiswaClass()
sistem.tambah_siswa("1001", "Andi Wijaya", "XII-A")
sistem.tambah_nilai("1001", 85)
sistem.tambah_nilai("1001", 90)

siswa = sistem.cari_siswa("1001")
if siswa:
    rata_rata = sistem.hitung_rata_rata("1001")
    print(f"\nNama: {siswa['nama']}")
    print(f"Kelas: {siswa['kelas']}")
    print(f"Rata-rata: {rata_rata:.1f}")

print("\n" + "=" * 60)
print("Created by: natedekaka")
print("=" * 60)
