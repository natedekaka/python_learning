# 📚 Kurikulum Python - SMAN Negeri 6 Cimahi
## Program Informatika - Kelas 10, 11, 12

---

## 📖 Pengenalan

Repository ini dirancang khusus untuk mendukung pembelajaran Python di SMAN Negeri 6 Cimahi dengan mengintegrasikan **Kurikulum Nasional/Merdeka** untuk program informatika.

**Sekolah:** SMAN Negeri 6 Cimahi  
**Program:** Informatika  
**Target Siswa:** Kelas X, XI, XII  
**Guru Pembimbing:** natedekaka

---

## 🎯 Capaian Pembelajaran

### **Kelas X (Fundamentals)**
- **Alur Tujuan Pembelajaran (ATP):**
  - Memahami konsep dasar pemrograman
  - Mengenal tipe data dan variabel
  - Membuat program dengan control flow
  - Membuat fungsi dan modularisasi kode

- **Materi:**
  - 01: Pengenalan Python & Variabel
  - 02: Tipe Data (String, Integer, Float, Boolean, List, Dictionary)
  - 03: Operator (Aritmatika, Perbandingan, Logika)
  - 04: Control Flow (if-else, loops)
  - 05: Fungsi (Function Definition, Parameters, Return)

- **Contoh Soal SMAN 6 Cimahi:**
  - Program data siswa SMAN 6 Cimahi
  - Sistem penilaian siswa
  - Manajemen nilai rapor

---

### **Kelas XI (Intermediate)**
- **Alur Tujuan Pembelajaran:**
  - Menguasai struktur data kompleks
  - Menggunakan file handling untuk I/O
  - Menangani exception
  - Membuat program dengan algoritma

- **Materi:**
  - 01: List & Dictionary Manipulation
  - 02: Nested Data Structure
  - 03: String Processing
  - 04: File Handling (Read, Write, Append)
  - 05: Exception Handling (Try-Except)
  - 06: Basic Algorithm & Sorting

- **Contoh Soal SMAN 6 Cimahi:**
  - Database guru & staf SMAN 6 Cimahi
  - Sistem inventaris lab komputer sekolah
  - Aplikasi presensi siswa dengan file CSV
  - Program pemindahan nilai siswa antar semester

---

### **Kelas XII (Advanced)**
- **Alur Tujuan Pembelajaran:**
  - Memahami OOP (Object-Oriented Programming)
  - Membuat aplikasi multi-file
  - Mengenal design patterns
  - Persiapan studi lanjut & industri

- **Materi:**
  - 01: Class & Object
  - 02: Inheritance & Polymorphism
  - 03: Encapsulation
  - 04: Module & Package
  - 05: Project-Based Learning

- **Contoh Soal SMAN 6 Cimahi:**
  - Sistem manajemen perpustakaan SMAN 6 Cimahi
  - Aplikasi penjadwalan kelas & guru
  - Sistem akademik terintegrasi (nilai, absensi, jadwal)
  - Portal siswa & orang tua SMAN 6 Cimahi

---

## 📂 Struktur Folder & Mapping Kurikulum

```
python_learning/

├── 01_fundamentals/          → KELAS X
│   ├── 01_data_types_variables.py        (ATP: Variabel & Tipe Data)
│   └── 02_practice_exercise.py           (ATP: Praktik Dasar)
│
├── 02_intermediate/          → KELAS XI
│   ├── 01_loops_conditions.py            (ATP: Control Flow Advanced)
│   ├── 02_functions_strings.py           (ATP: String & Function)
│   └── 03_files_exceptions.py            (ATP: File I/O & Exception)
│
├── 03_advanced/              → KELAS XII
│   ├── 01_oop_basics.py                  (ATP: OOP Fundamental)
│   └── 02_oop_exercise.py                (ATP: OOP Project)
│
├── exercises/                → LATIHAN PER LEVEL
│   ├── basics/               (Kelas X - Dasar)
│   ├── intermediate/         (Kelas XI - Intermediate)
│   └── advanced/             (Kelas XII - Advanced)
│
├── projects/                 → PROJECT SMAN 6 CIMAHI
│   ├── sistem_siswa_sman6.py
│   ├── inventaris_lab.py
│   ├── sistem_presensi.py
│   └── sistem_penilaian.py
│
└── references/
    ├── theory/               (Penjelasan Teori Lengkap)
    └── cheatsheets/          (Quick Reference)
```

---

## 🔄 Standar Variabel & Naming Convention

Untuk memastikan kode terstandar dan relevan dengan konteks SMAN 6 Cimahi:

### **Contoh Variabel Siswa:**
```python
# Data Siswa SMAN 6 Cimahi
nama_siswa = "Andi Wijaya"
nisn_siswa = "1234567890"
kelas_siswa = "X-A"
jurusan_siswa = "Informatika"
nilai_matematika = 85
nilai_bahasa_inggris = 78

# Data Guru SMAN 6 Cimahi
nama_guru = "Ibu Nadia"
nip_guru = "123456789"
mapel_guru = "Informatika"
kelas_ajar = ["X-A", "X-B", "XI-A"]

# Data Sekolah
nama_sekolah = "SMAN Negeri 6 Cimahi"
alamat_sekolah = "Jl. Marga Mulya No. 1, Cimahi"
tahun_akademik = 2024
semester = 1
```

### **Naming Conventions:**
- Variables: `snake_case` → `nama_siswa`, `nilai_rapor`
- Classes: `PascalCase` → `SiswaClass`, `GuruClass`
- Functions: `snake_case` → `hitung_nilai()`, `cari_siswa()`
- Constants: `UPPER_CASE` → `NAMA_SEKOLAH`, `TAHUN_AKADEMIK`

---

## 📋 Contoh Soal dengan Konteks SMAN 6 Cimahi

### **Kelas X - Level Dasar**
```python
# SOAL 1: Program Data Siswa Dasar
print("=" * 50)
print("SISTEM DATA SISWA SMAN 6 CIMAHI")
print("=" * 50)

# Input data siswa
nama_siswa = input("Masukkan nama siswa: ")
nisn = input("Masukkan NISN: ")
kelas = input("Masukkan kelas (X-A/X-B/X-C): ")
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

# Hitung rata-rata
nilai_rata = (nilai_uts + nilai_uas) / 2

# Tentukan grade
if nilai_rata >= 85:
    grade = "A"
elif nilai_rata >= 70:
    grade = "B"
else:
    grade = "C"

# Output
print(f"\nNama: {nama_siswa}")
print(f"NISN: {nisn}")
print(f"Kelas: {kelas}")
print(f"Nilai Rata-rata: {nilai_rata:.1f}")
print(f"Grade: {grade}")
```

### **Kelas XI - Level Intermediate**
```python
# SOAL: Program Manajemen Data Siswa SMAN 6 Cimahi
import json

# Data database siswa SMAN 6
data_siswa = {
    "1001": {"nama": "Andi Wijaya", "kelas": "XI-A", "nilai": [85, 90, 88]},
    "1002": {"nama": "Budi Santoso", "kelas": "XI-A", "nilai": [78, 82, 80]},
    "1003": {"nama": "Citra Dewi", "kelas": "XI-B", "nilai": [92, 95, 90]}
}

def cari_siswa_sman6(nisn):
    """Cari data siswa SMAN 6 berdasarkan NISN"""
    if nisn in data_siswa:
        siswa = data_siswa[nisn]
        rata_rata = sum(siswa["nilai"]) / len(siswa["nilai"])
        return siswa, rata_rata
    return None, None

def simpan_data_siswa(file_name):
    """Simpan data siswa SMAN 6 ke file JSON"""
    with open(file_name, 'w') as f:
        json.dump(data_siswa, f, indent=2)

# Program utama
nisn_cari = input("Masukkan NISN siswa SMAN 6 Cimahi: ")
siswa, rata_rata = cari_siswa_sman6(nisn_cari)

if siswa:
    print(f"Nama: {siswa['nama']}")
    print(f"Kelas: {siswa['kelas']}")
    print(f"Nilai Rata-rata: {rata_rata:.1f}")
else:
    print("Siswa tidak ditemukan di database SMAN 6 Cimahi")
```

### **Kelas XII - Level Advanced**
```python
# SOAL: Sistem Akademik SMAN 6 Cimahi (OOP)

class SiswaClass:
    """Class untuk data siswa SMAN 6 Cimahi"""
    
    def __init__(self, nisn, nama, kelas):
        self.nisn = nisn
        self.nama = nama
        self.kelas = kelas
        self.nilai_semester = []
    
    def tambah_nilai(self, nilai):
        """Tambahkan nilai siswa"""
        self.nilai_semester.append(nilai)
    
    def hitung_rata_rata(self):
        """Hitung rata-rata nilai siswa"""
        return sum(self.nilai_semester) / len(self.nilai_semester)
    
    def dapatkan_grade(self):
        """Dapatkan grade siswa"""
        rata_rata = self.hitung_rata_rata()
        if rata_rata >= 85:
            return "A"
        elif rata_rata >= 70:
            return "B"
        else:
            return "C"

# Implementasi
siswa_sman6 = SiswaClass("1001", "Andi Wijaya", "XII-A")
siswa_sman6.tambah_nilai(85)
siswa_sman6.tambah_nilai(90)
siswa_sman6.tambah_nilai(88)

print(f"Nama: {siswa_sman6.nama}")
print(f"Kelas: {siswa_sman6.kelas}")
print(f"Rata-rata: {siswa_sman6.hitung_rata_rata():.1f}")
print(f"Grade: {siswa_sman6.dapatkan_grade()}")
```

---

## 🎓 Kompetensi yang Dicapai

### **Kelas X:**
- ✅ Mengerti konsep variabel dan tipe data
- ✅ Dapat membuat program dengan kondisi & perulangan
- ✅ Mampu membuat fungsi sederhana
- ✅ Mengerti input-output dasar

### **Kelas XI:**
- ✅ Menguasai struktur data (list, dictionary)
- ✅ Dapat menangani file I/O
- ✅ Memahami exception handling
- ✅ Mampu membuat program modular

### **Kelas XII:**
- ✅ Menguasai OOP (class, inheritance, polymorphism)
- ✅ Dapat membuat aplikasi multi-file
- ✅ Mengerti design pattern dasar
- ✅ Siap untuk studi lanjut atau karir IT

---

## 📞 Kontak & Dukungan

**Sekolah:** SMAN Negeri 6 Cimahi  
**Guru Pembimbing:** natedekaka  
**Email:** [contact via SMAN 6 Cimahi]  
**Tahun Akademik:** 2024-2025

---

## 📄 Lisensi & Catatan

Repository ini dibuat khusus untuk mendukung pembelajaran di SMAN Negeri 6 Cimahi dan mengikuti kurikulum nasional/merdeka yang berlaku.

**Created by:** natedekaka  
**Last Updated:** 2026-04-10  
**Version:** 1.0.0

---

*Semangat belajar pemrograman! Untuk masa depan yang lebih baik. 🚀*
