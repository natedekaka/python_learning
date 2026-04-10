#!/usr/bin/env python3
"""
LATIHAN ADVANCED - SMAN Negeri 6 Cimahi
Program Informatika Kelas XII

Konteks: Sistem Akademik SMAN 6 Cimahi dengan OOP
Fitur: Management siswa, guru, nilai dengan class
"""

from datetime import datetime

# ===== CLASS SISWA SMAN 6 CIMAHI =====
class SiswaClass:
    """Class untuk merepresentasikan siswa SMAN 6 Cimahi"""
    
    def __init__(self, nisn, nama, kelas, jurusan="Informatika"):
        self.nisn = nisn
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan
        self.nilai_semester = []
        self.tgl_daftar = datetime.now().strftime("%Y-%m-%d")
    
    def tambah_nilai(self, nilai):
        """Tambahkan nilai siswa SMAN 6"""
        if 0 <= nilai <= 100:
            self.nilai_semester.append(nilai)
            return True
        return False
    
    def hitung_rata_rata(self):
        """Hitung rata-rata nilai siswa"""
        if len(self.nilai_semester) > 0:
            return sum(self.nilai_semester) / len(self.nilai_semester)
        return 0
    
    def dapatkan_grade(self):
        """Dapatkan grade siswa SMAN 6 Cimahi"""
        rata_rata = self.hitung_rata_rata()
        if rata_rata >= 85:
            return "A"
        elif rata_rata >= 70:
            return "B"
        elif rata_rata >= 55:
            return "C"
        else:
            return "D"
    
    def cek_kelulusan(self, nilai_minimum=70):
        """Cek apakah siswa lulus"""
        return self.hitung_rata_rata() >= nilai_minimum
    
    def tampilkan_data(self):
        """Tampilkan data siswa SMAN 6 Cimahi"""
        print("\n" + "=" * 70)
        print("DATA SISWA SMAN NEGERI 6 CIMAHI")
        print("=" * 70)
        print(f"NISN            : {self.nisn}")
        print(f"Nama            : {self.nama}")
        print(f"Kelas           : {self.kelas}")
        print(f"Jurusan         : {self.jurusan}")
        print(f"Tanggal Daftar  : {self.tgl_daftar}")
        print(f"Nilai Semester  : {self.nilai_semester}")
        print(f"Rata-rata       : {self.hitung_rata_rata():.2f}")
        print(f"Grade           : {self.dapatkan_grade()}")
        
        status = "✅ LULUS" if self.cek_kelulusan() else "❌ TIDAK LULUS"
        print(f"Status Kelulusan: {status}")
        print("=" * 70)

# ===== CLASS GURU SMAN 6 CIMAHI =====
class GuruClass:
    """Class untuk merepresentasikan guru SMAN 6 Cimahi"""
    
    def __init__(self, nip, nama, mapel):
        self.nip = nip
        self.nama = nama
        self.mapel = mapel
        self.kelas_ajar = []
    
    def tambah_kelas(self, nama_kelas):
        """Tambahkan kelas yang diajar"""
        if nama_kelas not in self.kelas_ajar:
            self.kelas_ajar.append(nama_kelas)
            return True
        return False
    
    def tampilkan_data(self):
        """Tampilkan data guru SMAN 6 Cimahi"""
        print(f"\n👨‍🏫 NIP: {self.nip}")
        print(f"   Nama: {self.nama}")
        print(f"   Mata Pelajaran: {self.mapel}")
        print(f"   Kelas Ajar: {', '.join(self.kelas_ajar) if self.kelas_ajar else 'Belum ada'}")

# ===== CLASS SISTEM AKADEMIK SMAN 6 =====
class SistemAkademikSMAN6:
    """Class untuk sistem akademik SMAN 6 Cimahi"""
    
    def __init__(self):
        self.daftar_siswa = {}
        self.daftar_guru = {}
        self.nama_sekolah = "SMAN Negeri 6 Cimahi"
        self.tahun_akademik = 2024
    
    def daftar_siswa_baru(self, nisn, nama, kelas, jurusan="Informatika"):
        """Daftarkan siswa baru SMAN 6 Cimahi"""
        if nisn not in self.daftar_siswa:
            siswa = SiswaClass(nisn, nama, kelas, jurusan)
            self.daftar_siswa[nisn] = siswa
            print(f"✅ Siswa {nama} berhasil didaftarkan di {self.nama_sekolah}")
            return siswa
        else:
            print(f"❌ NISN {nisn} sudah terdaftar")
            return None
    
    def cari_siswa(self, nisn):
        """Cari siswa SMAN 6 berdasarkan NISN"""
        return self.daftar_siswa.get(nisn)
    
    def daftar_guru_baru(self, nip, nama, mapel):
        """Daftarkan guru baru SMAN 6 Cimahi"""
        if nip not in self.daftar_guru:
            guru = GuruClass(nip, nama, mapel)
            self.daftar_guru[nip] = guru
            print(f"✅ Guru {nama} berhasil didaftarkan")
            return guru
        else:
            print(f"❌ NIP {nip} sudah terdaftar")
            return None
    
    def tampilkan_semua_siswa(self):
        """Tampilkan semua siswa SMAN 6 Cimahi"""
        print(f"\n📚 DAFTAR SISWA {self.nama_sekolah}")
        print("=" * 70)
        print(f"{'NISN':<10} {'Nama':<20} {'Kelas':<10} {'Rata-rata':<15}")
        print("-" * 70)
        
        for nisn, siswa in self.daftar_siswa.items():
            print(f"{nisn:<10} {siswa.nama:<20} {siswa.kelas:<10} {siswa.hitung_rata_rata():.2f}")
        print("=" * 70)

# ===== PROGRAM UTAMA =====
def main():
    print("\n" + "=" * 70)
    print("SISTEM AKADEMIK SMAN NEGERI 6 CIMAHI - OOP IMPLEMENTATION")
    print("Program Informatika - Kelas XII")
    print("=" * 70)
    
    # Inisialisasi sistem akademik
    sistem = SistemAkademikSMAN6()
    
    # 1️⃣ LATIHAN: Daftar siswa baru
    print("\n1️⃣  LATIHAN: MENDAFTARKAN SISWA BARU")
    print("-" * 70)
    
    siswa1 = sistem.daftar_siswa_baru("1001", "Andi Wijaya", "XII-A")
    siswa2 = sistem.daftar_siswa_baru("1002", "Budi Santoso", "XII-A")
    siswa3 = sistem.daftar_siswa_baru("1003", "Citra Dewi", "XII-B")
    
    # 2️⃣ LATIHAN: Input nilai siswa
    print("\n2️⃣  LATIHAN: INPUT NILAI SISWA")
    print("-" * 70)
    
    siswa1.tambah_nilai(85)
    siswa1.tambah_nilai(90)
    siswa1.tambah_nilai(88)
    print("✅ Nilai siswa SMAN 6 Cimahi berhasil diinput")
    
    siswa2.tambah_nilai(78)
    siswa2.tambah_nilai(82)
    siswa2.tambah_nilai(80)
    
    siswa3.tambah_nilai(92)
    siswa3.tambah_nilai(95)
    siswa3.tambah_nilai(90)
    
    # 3️⃣ LATIHAN: Tampilkan data siswa
    print("\n3️⃣  LATIHAN: MENAMPILKAN DATA SISWA")
    siswa1.tampilkan_data()
    
    # 4️⃣ LATIHAN: Daftar guru
    print("\n4️⃣  LATIHAN: MENDAFTARKAN GURU SMAN 6 CIMAHI")
    print("-" * 70)
    
    guru1 = sistem.daftar_guru_baru("NIP001", "Ibu Nadia", "Informatika")
    guru2 = sistem.daftar_guru_baru("NIP002", "Pak Sugeng", "Matematika")
    
    guru1.tambah_kelas("XII-A")
    guru1.tambah_kelas("XII-B")
    guru1.tampilkan_data()
    
    # 5️⃣ LATIHAN: Tampilkan semua siswa
    print("\n5️⃣  LATIHAN: TAMPILKAN SEMUA SISWA SMAN 6 CIMAHI")
    sistem.tampilkan_semua_siswa()
    
    print("\n" + "=" * 70)
    print("Program selesai - Dibuat untuk SMAN Negeri 6 Cimahi")
    print("=" * 70)

if __name__ == "__main__":
    main()
