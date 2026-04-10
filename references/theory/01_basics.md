# FASE 1: TEORI DASAR - Variables & Data Types

> 📚 Penjelasan singkat, mudah dipahami, dengan analogi dunia nyata

---

## 📝 Konsep Dasar

**Variable** adalah kotak penyimpanan yang menyimpan informasi. **Data Type** adalah jenis informasi apa yang disimpan.

---

## 🔍 Penjelasan Singkat

Bayangkan variable seperti **kotak penyimpanan di rumah**:
- Kotak untuk menyimpan **buku** (String) → menyimpan teks
- Kotak untuk menyimpan **koin** (Integer) → menyimpan angka bulat
- Kotak untuk menyimpan **emas batangan** (Float) → menyimpan angka desimal
- Kotak untuk menyimpan **stempel benar/salah** (Boolean) → menyimpan True/False

---

## 🌍 Analogi Dunia Nyata

### Kotak Penyimpanan

```
DUNIA NYATA                 PYTHON
─────────────────────────────────────────
Kotak penyimpanan    →      Variable
Apa yang disimpan    →      Value
Jenis kotak (besar/kecil) → Data Type

Contoh:
Nama saya: "Ari"           nama = "Ari"        (String)
Umur saya: 25 tahun        umur = 25           (Integer)
Tinggi saya: 1.75m         tinggi = 1.75       (Float)
Sudah menikah: Tidak       menikah = False     (Boolean)
```

### Visualisasi Memory

```
┌─────────────────────────────────┐
│      MEMORY KOMPUTER            │
│                                 │
│  ┌────────┐  ┌────────┐        │
│  │ nama   │  │ umur   │        │
│  │ "Ari"  │  │ 25     │        │
│  └────────┘  └────────┘        │
│                                 │
│  ┌──────────┐  ┌─────────┐    │
│  │ tinggi   │  │ menikah │    │
│  │ 1.75     │  │ False   │    │
│  └──────────┘  └─────────┘    │
│                                 │
└─────────────────────────────────┘
```

### Perbandingan Data Types

```
╔════════════╦════════════╦═══════════════╦════════════╗
║ Data Type  ║ Contoh     ║ Ukuran        ║ Kegunaan   ║
╠════════════╬════════════╬═══════════════╬════════════╣
║ String     ║ "Ari"      ║ Bervariasi    ║ Teks       ║
║ Integer    ║ 25         ║ 4-8 bytes     ║ Bilangan   ║
║ Float      ║ 1.75       ║ 8 bytes       ║ Desimal    ║
║ Boolean    ║ True/False ║ 1 byte        ║ Ya/Tidak   ║
╚════════════╩════════════╩═══════════════╩════════════╝
```

---

## 💡 Mengapa Penting?

### Alasan Teknis
- **Compiler/Interpreter perlu tahu** jenis data yang disimpan agar tahu cara memprosesnya
- **Mencegah error** - tidak bisa "tambah" teks dengan angka sembarangan
- **Efisiensi memori** - Integer hanya butuh 4 byte, String bisa lebih besar

### Alasan Praktis
- Program yang jelas = mudah di-debug
- Tahu output apa sebelum run
- Hindari bug yang sulit dicari

---

## ✅ Kapan Digunakan?

**Selalu!** Setiap program dimulai dengan menyimpan data dalam variable dengan type yang tepat.

### Contoh Kasus Nyata

| Kasus | Variable | Type | Alasan |
|-------|----------|------|--------|
| Nama user | `nama` | String | Menyimpan teks |
| Umur user | `umur` | Integer | Bilangan bulat |
| Tinggi badan | `tinggi` | Float | Bilangan desimal |
| Sudah login? | `is_login` | Boolean | Ya/Tidak |
| Harga barang | `harga` | Float | Nilai uang |
| ID user | `user_id` | Integer | Identitas unik |

---

## 🎓 Ringkasan Fase 1

| Aspek | Penjelasan |
|-------|-----------|
| **Apa itu Variable?** | Kotak untuk menyimpan data |
| **Apa itu Data Type?** | Jenis data yang disimpan |
| **Mengapa penting?** | Program jadi terstruktur & efisien |
| **Kapan pakai?** | Setiap saat dalam coding |
| **Analogi** | Kotak penyimpanan di rumah |

---

## 📌 Kode Contoh

```python
# Variables dengan berbagai data type
nama = "Ari"              # String
umur = 25                 # Integer
tinggi = 1.75             # Float
sudah_bekerja = True      # Boolean

# Print untuk lihat hasilnya
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Tinggi: {tinggi} meter")
print(f"Bekerja: {sudah_bekerja}")

# Type checking
print(type(nama))         # <class 'str'>
print(type(umur))         # <class 'int'>
print(type(tinggi))       # <class 'float'>
print(type(sudah_bekerja))# <class 'bool'>
```

**Output:**
```
Nama: Ari
Umur: 25 tahun
Tinggi: 1.75 meter
Bekerja: True
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

## 🚀 Lanjut ke Fase 2

Setelah menguasai Variables, fase berikutnya adalah **Data Structures** - cara menyimpan BANYAK data sekaligus.

👉 **Baca:** `11_TEORI_STRUKTUR_DATA.md`  
👉 **Kode:** `02_latihan.py` atau `quick_reference.py`

---

*Versi: 1.0 | Last Updated: 2026-04-10*
