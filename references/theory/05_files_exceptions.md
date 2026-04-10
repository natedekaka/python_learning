# FASE 5: TEORI FILE I/O & EXCEPTIONS - Simpan Data & Handle Error

> 📚 Cara menyimpan data ke file dan menangani error dengan elegan

---

## 📝 Konsep Dasar

**File I/O** = Baca/tulis data ke file. **Exceptions** = Tangani error dengan elegan.

---

## 🔍 Penjelasan Singkat

### FILE I/O - Membaca & Menulis Buku

```
Bayangkan file adalah buku di perpustakaan:

MENULIS (Write):
- Buku baru ditulis
- Setiap halaman adalah baris dalam file
- Jika sudah ada buku dengan nama sama → tulis ulang

MEMBACA (Read):
- Buka buku
- Baca halaman satu per satu
- Tutup buku setelah selesai

MENAMBAH (Append):
- Buka buku di halaman terakhir
- Tambah halaman baru
- Jangan hapus yang lama
```

---

## 🌍 Analogi Dunia Nyata

### FILE MODES - Jenis Akses File

```
┌─────────────────────────────────────┐
│          FILE OPERATIONS            │
│                                     │
│  "r" (Read)                         │
│  ├─ Buka file untuk dibaca          │
│  ├─ Hanya bisa baca                 │
│  └─ File harus sudah ada            │
│                                     │
│  "w" (Write)                        │
│  ├─ Buka file untuk ditulis         │
│  ├─ Buat file baru ATAU timpa       │
│  └─ Isi lama hilang!                │
│                                     │
│  "a" (Append)                       │
│  ├─ Buka file untuk ditambah        │
│  ├─ Tulis di akhir file             │
│  └─ Isi lama tetap ada              │
│                                     │
└─────────────────────────────────────┘
```

---

### EXCEPTIONS - Airbag di Mobil

```
Bayangkan exception handling seperti airbag:

NORMAL: Mobil jalan normal → tidak ada masalah

CRASH: Terjadi tabrakan
- Airbag langsung mengembang (try block berhenti)
- Mengurangi dampak (except block menghandle)
- Mobil masih bisa digunakan (program lanjut)

TANPA EXCEPTION HANDLING:
- Program crash → berhenti total
- User bingung apa yang salah

DENGAN EXCEPTION HANDLING:
- Program tangani error dengan elegan
- User dapat pesan yang jelas
- Program terus berjalan

Flowchart:
         START
           │
           ▼
       TRY (Coba)
       ╱        ╲
    SUKSES      ERROR
      │           │
      ▼           ▼
   Lanjut    EXCEPT (Tangkap)
      │           │
      ▼           ▼
   FINALLY (Cleanup)
      │
      ▼
     END
```

---

### COMMON EXCEPTIONS

```
ValueError:  Input tipe salah (input("angka"): "abc")
TypeError:   Operasi dengan tipe tidak cocok ("5" + 3)
IndexError:  Akses index yang tidak ada (list[10] saat list hanya 5 item)
KeyError:    Akses key yang tidak ada di dict (dict["tidak_ada"])
FileNotFoundError: File tidak ditemukan (open("nonexistent.txt"))
ZeroDivisionError: Bagi dengan 0 (100 / 0)
```

---

## 💡 Mengapa Penting?

### Alasan untuk File I/O

| Alasan | Penjelasan |
|---|---|
| **Persist Data** | Menyimpan data agar tidak hilang saat program ditutup |
| **Load Configuration** | Baca setting dari file config |
| **Process Large Data** | Baca data dari CSV/JSON |
| **Generate Reports** | Tulis hasil analysis ke file |

### Alasan untuk Exceptions

| Alasan | Penjelasan |
|---|---|
| **Program Robust** | Tidak crash meski ada error |
| **User-friendly** | Pesan error yang jelas bukan crash |
| **Data Safe** | Handle error sebelum data corrupt |
| **Logging** | Catat error untuk debugging |

---

## ✅ Kapan Digunakan?

| Konsep | Kapan Digunakan | Contoh |
|---|---|---|
| **File read** | Load data dari database, config, CSV | Baca data siswa dari file |
| **File write** | Simpan hasil proses ke file | Export laporan ke file |
| **File append** | Log data, menambah history | Catat activity ke log file |
| **Try/except** | Input dari user, buka file, API calls | Validasi input user |
| **Finally** | Cleanup resources (tutup file, close connection) | Jangan lupa close file |

---

## 📌 Kode Contoh

### FILE READ - Membaca Data

```python
# Membaca file
with open("data.txt", "r") as file:
    isi = file.read()  # Baca semua
    print(isi)

# Membaca per-baris
with open("data.txt", "r") as file:
    for baris in file:
        print(baris.strip())
```

### FILE WRITE - Menulis Data

```python
# Tulis file baru (atau timpa yang lama)
with open("output.txt", "w") as file:
    file.write("Baris pertama\n")
    file.write("Baris kedua\n")
    file.write("Baris ketiga\n")

# Hasil: 3 baris di file output.txt
```

### FILE APPEND - Menambah Data

```python
# Tambah data ke akhir file
with open("log.txt", "a") as file:
    file.write("2026-04-10: Program started\n")
    file.write("2026-04-10: Processing...\n")

# File lama tetap ada, data baru ditambah
```

### EXCEPTION HANDLING - Try/Except

```python
# Tanpa exception handling (CRASH):
saldo = 100
tarik = int(input("Berapa mau ditarik?"))  # User input "abc"
saldo = saldo - tarik  # CRASH! Tidak bisa kurangi dengan string

# Dengan exception handling (AMAN):
try:
    tarik = int(input("Berapa mau ditarik?"))  # Input "abc"
    saldo = saldo - tarik
except ValueError:  # Tangkap error input
    print("Masukkan angka yang benar!")
except:
    print("Error tidak terduga")
else:
    print(f"Saldo baru: {saldo}")  # Jika tidak ada error
finally:
    print("Transaksi selesai")  # Selalu dijalankan
```

### FILE + EXCEPTION - Read CSV dengan Error Handling

```python
import csv

try:
    with open("siswa.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Nama: {row[0]}, Nilai: {row[1]}")
except FileNotFoundError:
    print("File siswa.csv tidak ditemukan!")
except IndexError:
    print("Format CSV tidak sesuai!")
finally:
    print("Proses selesai")
```

---

## 🎓 Ringkasan Fase 5

| Aspek | Penjelasan |
|---|---|
| **File Read** | Buka & baca data dari file |
| **File Write** | Buat file baru atau timpa |
| **File Append** | Tambah data ke akhir file |
| **Try/Except** | Tangkap & handle error dengan elegan |
| **Finally** | Cleanup resources, selalu dijalankan |

---

## 🚀 Lanjut ke Fase 6

Setelah menguasai File I/O & Exceptions, fase berikutnya adalah **Object-Oriented Programming (OOP)** - cara mengorganisir kode dengan struktur yang lebih baik.

👉 **Baca:** `15_TEORI_OOP.md`  
👉 **Kode:** `06_oop.py` atau `quick_reference.py`

---

*Versi: 1.0 | Last Updated: 2026-04-10*
