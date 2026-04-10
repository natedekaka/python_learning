# FASE 3: TEORI KONTROL ALUR - If/Else & Loops

> 📚 Cara membuat program berpikir dan membuat keputusan

---

## 📝 Konsep Dasar

**Control Flow** adalah kemampuan program untuk membuat keputusan dan mengulang tindakan.

---

## 🔍 Penjelasan Singkat

Program tanpa control flow hanya bisa "jalan lurus" dari atas ke bawah. Control flow membuat program bisa:
- **Membuat keputusan** (if/else) - "jika cuaca hujan, ambil payung"
- **Mengulang tindakan** (loops) - "cek setiap siswa di kelas sampai semuanya terpantau"

---

## 🌍 Analogi Dunia Nyata

### IF/ELSE/ELIF - Perjalanan ke Sekolah

```
Cerita: Besok mau ke sekolah

if cuaca == "hujan":
    ambil payung
    gunakan jas hujan
elif cuaca == "panas":
    pakai topi
    bawa botol minum
elif cuaca == "sejuk":
    normal saja
else:
    cek prakiraan cuaca lagi
    
Analogi:
- Keputusan berdasarkan kondisi
- Hanya 1 cabang yang dijalankan
- Sesuai dengan kondisi yang cocok
```

### Flowchart IF/ELSE

```
           START
             │
             ▼
       Cek cuaca?
       ╱    │    ╲
    Hujan  Panas  Lainnya
    ╱      │        ╲
   ▼       ▼        ▼
Ambil   Pakai    Cek
Payung  Topi     Lagi
   │      │        │
   ▼      ▼        ▼
  END    END      END
```

---

### FOR LOOP - Memanggil Absen di Kelas

```
CERITA: Guru memanggil absen

for siswa in daftar_siswa:
    panggil(siswa)
    catat_kehadiran(siswa)
    
Analogi:
- Guru tahu berapa siswa (jumlahnya terbatas)
- Guru memanggil satu per satu
- Sampai semua siswa selesai dipanggil
- Kemudian keluar dari loop

Mirip dengan:
- for i in range(30): → Panggil 30 siswa
- for item in shopping_list: → Belanja setiap item
```

### Visualisasi FOR LOOP

```
DAFTAR SISWA: ["Ari", "Budi", "Citra", "Doni"]

Iterasi 1: siswa = "Ari"   → Panggil Ari
Iterasi 2: siswa = "Budi"  → Panggil Budi
Iterasi 3: siswa = "Citra" → Panggil Citra
Iterasi 4: siswa = "Doni"  → Panggil Doni

SELESAI!
```

---

### WHILE LOOP - Antrian di Kasir

```
CERITA: Antri di kasir minimarket

while ada_orang_di_depan:
    tunggu
    jika sudah giliran saya:
        bayar
        bawa barang
        keluar dari antrian
    
Analogi:
- Kita tidak tahu berapa lama (tidak tahu jumlah pastinya)
- Terus tunggu SAMPAI kondisi berubah
- Ketika tidak ada orang → keluar dari loop
- Bisa infinite loop jika tidak ada yang selesai!

Mirip dengan:
- while uang_belum_cukup: → Terus menabung
- while password_salah: → Coba login lagi
```

### Flowchart WHILE LOOP

```
     START
       │
       ▼
   Ada orang?
    ╱      ╲
   YA      TIDAK
   │         │
   ▼         ▼
 Tunggu    SELESAI
   │
   ▼
 Bayar
   │
   ▼
 Bawa barang
   │
   ▼
 Kembali cek (ada orang?)
```

---

### NESTED LOOP - Mencetak Jadwal Pelajaran

```
CERITA: Buat tabel jadwal pelajaran

for hari in ["Senin", "Selasa", "Rabu"]:
    for jam in ["08.00", "09.00", "10.00"]:
        print(f"{hari} jam {jam}")

Hasil:
Senin jam 08.00
Senin jam 09.00
Senin jam 10.00
Selasa jam 08.00
Selasa jam 09.00
Selasa jam 10.00
Rabu jam 08.00
Rabu jam 09.00
Rabu jam 10.00
        
Analogi:
- Loop luar: Setiap hari
- Loop dalam: Setiap jam di hari itu
- Seperti membuat matriks/grid
```

---

## 💡 Mengapa Penting?

### Alasan untuk Setiap Control Flow

| Control Flow | Alasan Penting |
|---|---|
| **if/else** | Program bisa "berpikir" dan membuat keputusan |
| **for** | Otomasi tugas repetitif yang sudah terbatas |
| **while** | Otomasi tugas yang belum tahu kapan selesai |
| **nested** | Menangani masalah yang lebih kompleks |

---

## ✅ Kapan Digunakan?

| Control Flow | Kapan Digunakan | Contoh |
|---|---|---|
| **if/else** | Validasi input, grading, memberikan rekomendasi | Cek apakah nilai lulus/tidak |
| **for** | Proses setiap item di list, countdown | Hitung nilai ujian semua siswa |
| **while** | Login loop, animasi, processing sampai kondisi tercapai | Retry password sampai benar |
| **nested** | Tabel, matriks, struktur berlapis | Jadwal kelas dengan hari & jam |

---

## 📌 Kode Contoh

### IF/ELSE - Sistem Grading

```python
nilai = 85

if nilai >= 80:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Nilai: {nilai} → Grade: {grade}")  # Grade: A
```

### FOR LOOP - Menghitung Nilai Rata-rata

```python
nilai_ujian = [80, 85, 90, 95]
total = 0

for nilai in nilai_ujian:
    total = total + nilai

rata_rata = total / len(nilai_ujian)
print(f"Rata-rata: {rata_rata}")  # 87.5
```

### WHILE LOOP - Login System

```python
password_benar = "python123"
coba = 0

while True:
    password = input("Masukkan password: ")
    coba += 1
    
    if password == password_benar:
        print("Login berhasil!")
        break
    elif coba >= 3:
        print("Terlalu banyak kesalahan!")
        break
    else:
        print("Password salah, coba lagi")
```

### NESTED LOOP - Tabel Perkalian

```python
for i in range(1, 4):      # Baris 1-3
    for j in range(1, 4):  # Kolom 1-3
        print(f"{i}×{j}={i*j}", end=" ")
    print()  # Pindah baris

# Hasil:
# 1×1=1 1×2=2 1×3=3
# 2×1=2 2×2=4 2×3=6
# 3×1=3 3×2=6 3×3=9
```

---

## 🎓 Ringkasan Fase 3

| Aspek | Penjelasan |
|---|---|
| **if/else** | Membuat keputusan berdasarkan kondisi |
| **for** | Loop dengan jumlah iterasi yang tahu |
| **while** | Loop sampai kondisi tidak terpenuhi |
| **nested** | Loop dalam loop untuk struktur kompleks |

---

## 🚀 Lanjut ke Fase 4

Setelah menguasai Control Flow, fase berikutnya adalah **Functions & Strings** - cara membuat kode reusable dan manipulasi teks.

👉 **Baca:** `13_TEORI_FUNGSI_STRING.md`  
👉 **Kode:** `04_functions_strings.py` atau `quick_reference.py`

---

*Versi: 1.0 | Last Updated: 2026-04-10*
