#!/usr/bin/env python3
"""
==========================================
LATIHAN 1: DATA DIRI
==========================================
Tujuan: Memahami cara membuat variabel dan menampilkan output

Konsep yang dipelajari:
- Variabel (String, Integer, Float, Boolean)
- print() function
- f-string formatting

==========================================
"""

# ==============================
# BAGIAN 1: BUAT VARIABEL DATA DIRI
# ==============================

# TODO 1: Isi data diri kamu di bawah ini
nama = "..."           # Ganti dengan namamu
umur = ...             # Ganti dengan umurm
tinggi = ...           # Ganti dengan tinggimu (contoh: 1.65)
kelas = "..."          # Ganti dengan kelasmu
sekolah = "..."        # Ganti dengan nama sekolahmu
hobi = [...]           # Isi 3 hobimu dalam list

# ==============================
# BAGIAN 2: TAMPILKAN DATA
# ==============================

print("=" * 40)
print("�️  DATA DIRI SAYA")
print("=" * 40)

# TODO 2: Tampilkan semua data dengan format yang menarik
print(f"Nama    : {nama}")
print(f"Umur    : {umur} tahun")
print(f"Tinggi  : {tinggi} m")
print(f"Kelas   : {kelas}")
print(f"Sekolah : {sekolah}")
print(f"Hobi    : {hobi}")

# ==============================
# BAGIAN 3: HITUNG RUMUS SEDERHANA
# ==============================

print("\n" + "=" * 40)
print("🧮 HASIL PERHITUNGAN")
print("=" * 40)

# TODO 3: Hitung usia 5 tahun lagi
usia_5_tahun_lagi = ...
print(f"Usia 5 tahun lagi: {usia_5_tahun_lagi} tahun")

# TODO 4: Tinggi dalam cm
tinggi_cm = ...
print(f"Tinggi dalam cm: {tinggi_cm} cm")

# TODO 5: Jumlah karakter nama
jumlah_huruf = ...
print(f"Jumlah huruf dalam nama: {jumlah_huruf}")

# ==============================
# BAGIAN 4: TIPE DATA
# ==============================

print("\n" + "=" * 40)
print("📋 TIPE DATA")
print("=" * 40)

# TODO 6: Tampilkan tipe data dari setiap variabel
print(f"nama     -> {type(nama)}")
print(f"umur     -> {type(umur)}")
print(f"tinggi   -> {type(tinggi)}")
print(f"hobi     -> {type(hobi)}")

print("\n✅ Latihan 1 Selesai!")
