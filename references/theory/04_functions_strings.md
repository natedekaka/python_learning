# FASE 4: TEORI FUNGSI & STRING - Kode Reusable & Manipulasi Teks

> 📚 Cara membuat kode yang bisa dipakai berkali-kali dan manipulasi teks

---

## 📝 Konsep Dasar

**Function** adalah blok kode yang dapat digunakan berkali-kali. **String** adalah teks yang dapat dimanipulasi.

---

## 🔍 Penjelasan Singkat

### FUNCTIONS - Mesin Kopi

```
Bayangkan mesin kopi:

Input: Biji kopi, air, gula
Proses: Grinding, brewing
Output: Kopi siap minum

ANALOGI:
def buat_kopi(biji_kopi, air, gula):
    # Proses di dalam mesin
    grinding(biji_kopi)
    hasil = brewing(biji_kopi, air)
    hasil = tambah_gula(hasil, gula)
    return hasil  # Output

kopi_saya = buat_kopi("arabika", 200, 2)
```

**Mengapa pakai function?**
- Tidak perlu ulangi kode grinding, brewing, tambahin gula lagi
- Cukup panggil `buat_kopi()` berapa kali saja
- Jika mau ubah resep → ubah di 1 tempat saja

---

## 🌍 Analogi Dunia Nyata

### FUNCTIONS - Struktur Input/Process/Output

```
┌─────────────────────────────────────┐
│         MESIN KOPI (Function)       │
│                                     │
│  INPUT                              │
│  ├─ Biji kopi                       │
│  ├─ Air                             │
│  └─ Gula                            │
│         │                           │
│         ▼                           │
│  PROCESS                            │
│  ├─ Grinding                        │
│  ├─ Brewing                         │
│  └─ Mix dengan gula                 │
│         │                           │
│         ▼                           │
│  OUTPUT: Kopi siap minum ☕          │
│                                     │
└─────────────────────────────────────┘
```

---

### STRINGS - Teks yang Bisa Dimanipulasi

```
Bayangkan teks adalah tanah liat:

Teks original: "  Belajar Python  "

Operasi:
- .strip()     → Hilangkan spasi kosong
- .upper()     → Ubah jadi HURUF BESAR
- .lower()     → Ubah jadi huruf kecil
- .replace()   → Ganti kata
- .split()     → Potong berdasarkan pemisah
- .join()      → Gabung dengan pemisah
- .find()      → Cari posisi kata
```

### Visualisasi String Operations

```
ORIGINAL: "  Belajar Python  "

.strip()  →  "Belajar Python"     (hilang spasi)
.upper()  →  "BELAJAR PYTHON"     (besar semua)
.lower()  →  "belajar python"     (kecil semua)
.replace("Python", "Java")  →  "Belajar Java"
.split()  →  ["Belajar", "Python"]  (potong jadi list)
```

---

### LIST COMPREHENSION - Shortcut Masak

```
CARA BIASA:
karung_beras = [10, 15, 8, 12, 20]  # kg
hasil = []
for berat in karung_beras:
    hasil.append(berat * 2)  # Dobel setiap karung
# Hasil: [20, 30, 16, 24, 40]

CARA CEPAT (LIST COMPREHENSION):
hasil = [berat * 2 for berat in karung_beras]

ANALOGI:
- Biasa = Harus mengambil setiap karung, membukanya, menambah isinya
- Cepat = Gunakan mesin otomatis yang langsung dobel semua
```

---

### LAMBDA - Fungsi Anonymous (Tanpa Nama)

```
Bayangkan lambda seperti sticky notes:

FUNCTION BIASA (dengan nama):
def kali_2(x):
    return x * 2

LAMBDA (tanpa nama, sticky note):
lambda x: x * 2

Gunakan dengan map/filter:
numbers = [1, 2, 3, 4, 5]
hasil = list(map(lambda x: x * 2, numbers))
# Hasil: [2, 4, 6, 8, 10]
```

---

## 💡 Mengapa Penting?

### Alasan untuk Setiap Konsep

| Konsep | Alasan Penting |
|---|---|
| **Functions** | Hindari repeat kode (DRY = Don't Repeat Yourself) |
| **Strings** | Manipulasi teks sangat sering di program nyata |
| **Comprehension** | Kode lebih ringkas dan cepat |
| **Lambda** | Fungsi simple yang hanya 1-2 baris |

---

## ✅ Kapan Digunakan?

| Konsep | Kapan Digunakan | Contoh |
|---|---|---|
| **Functions** | Kode yang dipakai 2+ kali | Hitung rata-rata, validasi input |
| **String methods** | Input/output, data cleaning | Hilang spasi, ubah format |
| **Comprehension** | Transform list/dict dengan singkat | Ubah satuan, filter data |
| **Lambda** | Fungsi simple 1-2 baris | Sorting custom, map/filter |

---

## 📌 Kode Contoh

### FUNCTIONS - Menghitung Luas Persegi Panjang

```python
def hitung_luas(panjang, lebar):
    """Fungsi untuk menghitung luas persegi panjang"""
    luas = panjang * lebar
    return luas

# Gunakan berkali-kali
luas1 = hitung_luas(10, 5)   # 50
luas2 = hitung_luas(20, 8)   # 160

print(f"Luas 1: {luas1}")
print(f"Luas 2: {luas2}")
```

### STRINGS - Manipulasi Teks

```python
text = "  belajar python  "

# String methods
print(text.strip())           # "belajar python"
print(text.upper())           # "  BELAJAR PYTHON  "
print(text.replace("python", "java"))  # "  belajar java  "
print(text.split())           # ["belajar", "python"]

# String formatting
nama = "Ari"
umur = 25
print(f"Nama: {nama}, Umur: {umur}")  # Nama: Ari, Umur: 25
```

### LIST COMPREHENSION - Transform List

```python
# Kalikan 2 untuk setiap angka
numbers = [1, 2, 3, 4, 5]
hasil = [x * 2 for x in numbers]
print(hasil)  # [2, 4, 6, 8, 10]

# Filter angka genap saja
hasil = [x for x in numbers if x % 2 == 0]
print(hasil)  # [2, 4]

# Dari list dict
siswa = [
    {"nama": "Ari", "nilai": 80},
    {"nama": "Budi", "nilai": 85}
]
nama_list = [s["nama"] for s in siswa]
print(nama_list)  # ["Ari", "Budi"]
```

### LAMBDA - Fungsi Tanpa Nama

```python
# Lambda dengan map
numbers = [1, 2, 3, 4, 5]
hasil = list(map(lambda x: x * 2, numbers))
print(hasil)  # [2, 4, 6, 8, 10]

# Lambda dengan filter
hasil = list(filter(lambda x: x > 2, numbers))
print(hasil)  # [3, 4, 5]

# Lambda dengan sorted (sort custom)
nama = ["Ari", "Budi", "Citra"]
sorted_nama = sorted(nama, key=lambda x: len(x))
print(sorted_nama)  # ["Ari", "Budi", "Citra"] (by length)
```

---

## 🎓 Ringkasan Fase 4

| Aspek | Penjelasan |
|---|---|
| **Functions** | Blok kode reusable dengan input/output |
| **Strings** | Teks yang bisa dimanipulasi dengan methods |
| **Comprehension** | Cara singkat transform list/dict |
| **Lambda** | Fungsi anonymous simple & concise |

---

## 🚀 Lanjut ke Fase 5

Setelah menguasai Functions & Strings, fase berikutnya adalah **File I/O & Exceptions** - cara menyimpan data dan handle error.

👉 **Baca:** `14_TEORI_FILE_EXCEPTION.md`  
👉 **Kode:** `05_files_exceptions.py` atau `quick_reference.py`

---

*Versi: 1.0 | Last Updated: 2026-04-10*
