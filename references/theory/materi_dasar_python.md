# Modul 1: Fundamental Pemrograman Python (Standard Internasional)
**Target:** Memahami arsitektur data, manajemen memori dasar, dan logika komputasi.

---

## 1. Pendahuluan: Karakteristik Bahasa
*   **Definisi Akademik:** Python adalah bahasa pemrograman **High-Level**, **Interpreted**, dan **General-Purpose**. Python menggunakan **Interpreted execution model**, di mana kode sumber dijalankan baris demi baris oleh Python Interpreter tanpa perlu proses kompilasi eksplisit ke kode mesin oleh pengguna.
*   **Analogi:** Jika bahasa mesin adalah kode Morse yang rumit, Python adalah memo yang ditulis dengan rapi dalam bahasa Inggris formal yang mudah dipahami manusia namun tetap presisi bagi komputer.

---

## 2. Variabel & Identifier (Memory Management)
*   **Definisi Akademik:** Variabel dalam Python adalah **Identifier** yang berfungsi sebagai **Reference** (referensi) atau label menuju sebuah **Object** di dalam memori (RAM). Python menerapkan **Reference Semantics**, di mana variabel tidak "menyimpan" nilai secara langsung, melainkan menyimpan alamat memori dari objek tersebut.
*   **Analogi:** Kotak penyimpanan dengan label di gudang. Nama pada label adalah Identifier, dan isi kotak adalah Object-nya.
*   **Naming Conventions (PEP 8):**
    1.  **Alphanumeric:** Dimulai dengan huruf (a-z) atau underscore (`_`).
    2.  **Case-Sensitivity:** Python bersifat *case-sensitive* (membedakan huruf besar dan kecil).
    3.  **Reserved Keywords:** Tidak boleh menggunakan kata kunci sistem (seperti `class`, `def`, `if`).

---

## 3. Tipe Data (Data Classification)
Python adalah bahasa **Strongly, Dynamically Typed**.
*   **Strongly Typed:** Sistem tidak akan secara otomatis mengubah tipe data secara tidak logis (misal: menjumlahkan string dan integer akan menghasilkan error).
*   **Dynamically Typed:** Tipe data variabel ditentukan pada saat *runtime* (ketika program berjalan) berdasarkan nilai yang di-assign padanya.

| Tipe (Class) | Deskripsi Akademik | Analogi |
| :--- | :--- | :--- |
| `str` (String) | **Immutable sequence** of Unicode characters. | Teks atau rangkaian karakter. |
| `int` (Integer) | **Arbitrary-precision** integers (bilangan bulat tak terbatas). | Bilangan bulat (jumlah unit). |
| `float` (Float) | **Double-precision floating point** (standard IEEE 754). | Bilangan desimal/pecahan. |
| `bool` (Boolean) | **Logical data type** dengan dua nilai literal: `True` atau `False`. | Saklar On/Off (Logika Biner). |

---

## 4. Operator & Expression
### A. Arithmetic Operators
Digunakan untuk membentuk **Arithmetic Expressions**.
*   `+` (Addition), `-` (Subtraction), `*` (Multiplication), `/` (True Division).
*   `//` (**Floor Division**): Menghasilkan nilai *quotient* (hasil bagi) dalam bentuk integer dengan membuang sisa desimal.
*   `%` (**Modulo**): Menghasilkan *remainder* (sisa) dari operasi pembagian.
*   `**` (**Exponentiation**): Operasi pemangkatan.

### B. Relational (Comparison) Operators
Menghasilkan nilai **Boolean**. Digunakan untuk mengevaluasi hubungan antara dua operand.
*   `==` (Equality), `!=` (Inequality), `>`, `<`, `>=`, `<=`.

### C. Logical Operators
Digunakan untuk menggabungkan beberapa pernyataan Boolean (**Short-circuit evaluation**).
*   `and` : Menghasilkan `True` jika kedua operand benar.
*   `or`  : Menghasilkan `True` jika salah satu operand benar.
*   `not` : **Logical negation** (membalikkan nilai kebenaran).

---

## 5. Input, Output, & Type Conversion
*   **Standard Output:** Menggunakan fungsi `print()` untuk mengirim data ke *standard output stream*.
*   **Standard Input:** Fungsi `input()` menghentikan eksekusi dan menunggu data dari user. **Penting:** Input selalu mengembalikan tipe data `str`.
*   **Type Casting (Explicit Conversion):** Proses mengubah objek dari satu tipe ke tipe lain secara manual (misal: `int()`, `float()`, `str()`).

---

## 6. Panduan Praktik (Laboratory Exercises)

### File 01: `01_variable_analysis.py`
```python
# Demonstrasi Dynamic Typing
data = "Universitas"
print(f"Nilai: {data}, Tipe: {type(data)}")

data = 2026
print(f"Nilai: {data}, Tipe: {type(data)}")
```

### File 02: `02_scientific_calculator.py`
```python
# Input & Arithmetic Expression
radius = float(input("Masukkan jari-jari lingkaran: "))
pi = 3.14159
area = pi * (radius ** 2)

print(f"Luas Lingkaran: {area:.2f}")
```

### File 03: `03_logic_validation.py`
```python
# Relational & Logical Operators
usia = int(input("Masukkan usia: "))
punya_ktp = True

# Syarat Memilih: Usia >= 17 DAN memiliki KTP
bisa_memilih = (usia >= 17) and punya_ktp

print(f"Status Hak Pilih: {bisa_memilih}")
```

---

## 7. Troubleshooting & Debugging
1.  **SyntaxError:** Pelanggaran terhadap aturan tata bahasa Python.
2.  **TypeError:** Operasi dilakukan pada tipe data yang tidak kompatibel.
3.  **ValueError:** Fungsi menerima argumen dengan tipe yang benar tetapi nilai yang tidak sesuai (misal: `int("abc")`).
4.  **NameError:** Mencoba mengakses identifier yang belum didefinisikan dalam lingkup (*scope*) saat ini.

---

## 8. Latihan Formatif (Assessment)
1.  **Sistem Kasir:** Buatlah program yang menghitung total belanja setelah diskon 10%.
2.  **Konversi Unit:** Buatlah konversi suhu dari Celcius ke Kelvin. (K = C + 273.15).
3.  **Evaluasi Logika:** Buatlah pengecekan apakah sebuah angka adalah bilangan genap (gunakan operator `%`).

---
**Pedagogi:** Fokuskan pada pemahaman bahwa Python memanipulasi **Object** dan **Reference**, bukan sekadar "menyimpan angka dalam kotak". Ini akan memudahkan saat nanti belajar List dan Dictionary.
