# FASE 2: TEORI STRUKTUR DATA - List, Dict, Tuple, Set

> 📚 Cara mengorganisir banyak data dengan efisien

---

## 📝 Konsep Dasar

**Data Structure** adalah cara mengorganisir banyak data agar mudah diakses dan diproses.

---

## 🔍 Penjelasan Singkat

Jika Fase 1 tentang "kotak satu item", Fase 2 tentang "rak penyimpanan":

1. **List** = Rak berisi barang dengan urutan (0, 1, 2, ...)
2. **Dictionary** = Lemari dengan label (nama → nilai)
3. **Tuple** = Rak yang tidak boleh diubah (immutable)
4. **Set** = Kontainer yang tidak boleh ada duplikat

---

## 🌍 Analogi Dunia Nyata

### LIST - Barisan Antrian Bioskop

```
LIST: [Ari, Budi, Citra, Doni]

Index:  0    1     2      3

Analogi:
- Ari ada di posisi 0 (paling depan)
- Budi ada di posisi 1
- Citra ada di posisi 2
- Doni ada di posisi 3 (paling belakang)

Operasi:
- Tambah (append): Orang baru datang ke belakang antrian
- Hapus (remove): Orang keluar dari antrian
- Akses: Kita tahu siapa yang di posisi ke-2
```

### Visualisasi LIST

```
INDEX:    0      1      2       3
         ┌──────┬──────┬──────┬──────┐
LIST:    │ Ari  │ Budi │Citra │Doni  │
         └──────┴──────┴──────┴──────┘
         ▲                           ▲
       HEAD                        TAIL
     (Depan)                     (Belakang)

AKSES:
list[0]   → "Ari"
list[2]   → "Citra"
list[-1]  → "Doni"  (dari belakang)
```

---

### DICTIONARY - Buku Telepon

```
DICTIONARY: {
    "Ari": "0812345678",
    "Budi": "0823456789",
    "Citra": "0834567890"
}

Analogi:
- Kita tidak perlu tahu halaman berapa
- Kita langsung cari NAMA → dapat NOMOR
- Lebih cepat daripada cari di list

Operasi:
- Tambah: Isi kontak baru di buku telepon
- Akses: Cari nama Ari → dapat nomornya
- Ubah: Update nomor Budi yang lama

Visualisasi:
       NAMA           NOMOR
  ┌─────────────┬─────────────┐
  │             │             │
  │  "Ari"  ←→  │ "0812345678"│
  │             │             │
  ├─────────────┼─────────────┤
  │             │             │
  │  "Budi" ←→  │ "0823456789"│
  │             │             │
  ├─────────────┼─────────────┤
  │             │             │
  │ "Citra" ←→  │ "0834567890"│
  │             │             │
  └─────────────┴─────────────┘

AKSES:
dict["Ari"]   → "0812345678"
dict["Budi"]  → "0823456789"
```

---

### TUPLE - Himpunan Pemain Sepak Bola

```
TUPLE: (Kiper, Bek, Gelandang, Penyerang)

Analogi:
- Tidak bisa diubah (immutable)
- Format tetap sama setiap pertandingan
- Jika ingin ubah, harus buat tuple baru

Mengapa immutable?
- Melindungi data dari perubahan tidak disengaja
- Lebih cepat karena tidak perlu cek perubahan
- Aman untuk data yang tidak boleh berubah

Contoh:
tuple_tetap = (1, 2, 3)
# tuple_tetap[0] = 10  ← ERROR!
# Tuple tidak bisa dimodifikasi
```

---

### SET - Daftar Tamu Undangan (Tidak Boleh Duplikat)

```
SET: {Ari, Budi, Citra}

Analogi:
- Setiap orang hanya terdaftar sekali
- Jika nama Ari ditambah lagi → tetap 1 (tidak ada duplikat)
- Tidak ada urutan pasti

Visualisasi:
   ┌─────────────────────────┐
   │      SET: {A, B, C}     │
   │                         │
   │   ●A        ●B          │
   │                         │
   │          ●C             │
   │                         │
   │  TIDAK ADA DUPLIKAT!    │
   │  TIDAK ADA URUTAN!      │
   └─────────────────────────┘

JIKA TAMBAH A LAGI:
{A, B, C}.add(A)  → Tetap {A, B, C}

Operasi:
- Union: Gabung 2 daftar tamu
- Intersection: Orang yang ada di 2 undangan
- Difference: Orang yang hanya di undangan A
```

---

## 💡 Mengapa Penting?

### Alasan untuk Setiap Struktur

| Struktur | Alasan Penting |
|----------|---|
| **List** | Menyimpan banyak data yang urut dan mungkin berubah |
| **Dictionary** | Akses data dengan "label" lebih cepat dari list |
| **Tuple** | Data yang pasti tidak boleh berubah |
| **Set** | Memastikan tidak ada duplikat |

---

## ✅ Kapan Digunakan?

### Tabel Penggunaan

| Struktur | Kapan Digunakan | Contoh |
|----------|---|---|
| **List** | Nilai ujian siswa, antrian, to-do list | `[80, 85, 90, 95]` |
| **Dictionary** | Data siswa (nama→nilai), kontak telepon | `{"Ari": 80, "Budi": 85}` |
| **Tuple** | Koordinat (x, y), tanggal tetap | `(10, 20)`, `(2026, 4, 10)` |
| **Set** | Tag unik, daftar tanpa duplikat | `{"Python", "Java", "Go"}` |

---

## 📌 Kode Contoh

### LIST - Menyimpan Nilai Ujian

```python
nilai_ujian = [80, 85, 90, 95]

# Tambah nilai baru
nilai_ujian.append(88)  # [80, 85, 90, 95, 88]

# Hapus nilai
nilai_ujian.remove(85)  # [80, 90, 95, 88]

# Akses berdasarkan index
print(nilai_ujian[0])   # 80
print(nilai_ujian[-1])  # 88 (yang terakhir)
```

### DICTIONARY - Menyimpan Kontak

```python
kontak = {
    "Ari": "0812345678",
    "Budi": "0823456789",
    "Citra": "0834567890"
}

# Akses kontak
print(kontak["Ari"])    # 0812345678

# Tambah kontak baru
kontak["Doni"] = "0845678901"

# Update kontak
kontak["Ari"] = "0812999999"
```

### TUPLE - Menyimpan Koordinat

```python
titik = (10, 20)

# Akses seperti list
print(titik[0])  # 10
print(titik[1])  # 20

# TIDAK bisa dimodifikasi
# titik[0] = 15  ← ERROR!
```

### SET - Menyimpan Tag Unik

```python
tag = {"Python", "Java", "Go"}

# Tambah tag
tag.add("Rust")        # {"Python", "Java", "Go", "Rust"}

# Tambah tag yang sama (tidak ada efek)
tag.add("Python")      # Masih {"Python", "Java", "Go", "Rust"}

# Hapus tag
tag.remove("Java")     # {"Python", "Go", "Rust"}
```

---

## 🎓 Ringkasan Fase 2

| Aspek | Penjelasan |
|-------|---|
| **List** | Array urutan, bisa dimodifikasi |
| **Dictionary** | Pasangan key-value, akses cepat |
| **Tuple** | Array urutan, tidak bisa dimodifikasi |
| **Set** | Himpunan unik, tidak ada duplikat |

---

## 🚀 Lanjut ke Fase 3

Setelah menguasai Data Structures, fase berikutnya adalah **Control Flow** - cara membuat program berpikir & membuat keputusan.

👉 **Baca:** `12_TEORI_KONTROL_ALUR.md`  
👉 **Kode:** `03_loops_conditions.py` atau `quick_reference.py`

---

*Versi: 1.0 | Last Updated: 2026-04-10*
