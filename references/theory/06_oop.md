# FASE 6: TEORI OOP - Object-Oriented Programming

> 📚 Cara mengorganisir kode dengan struktur blueprint yang elegant

---

## 📝 Konsep Dasar

**OOP** adalah cara mengorganisir kode dengan membuat "blueprint" untuk membuat object yang lebih terstruktur.

---

## 🔍 Penjelasan Singkat

### CLASS - Cetak Kue

```
Bayangkan class seperti cetakan kue:

CETAKAN (Class):
- Blueprint untuk membuat banyak kue
- Desain sudah terdefinisi
- Bisa reusable berkali-kali

KUENYA (Object/Instance):
- Produk nyata dari cetakan
- Bisa ada banyak kue dari 1 cetakan
- Masing-masing kue independent (kue A tidak pengaruh kue B)

CONTOH KODE:
class KueBiscuit:          # Cetakan kue
    def __init__(self):     # Setup awal
        self.rasa = "vanilla"
    
    def panggang(self):     # Method
        self.rasa = "cokelat"

kue1 = KueBiscuit()  # Instance 1
kue2 = KueBiscuit()  # Instance 2
```

---

## 🌍 Analogi Dunia Nyata

### INHERITANCE - Keluarga Besar

```
Bayangkan inheritance seperti sifat turun temurun:

ORANG TUA (Parent Class):
- Punya sifat umum (mata, hidung, telinga)
- Punya kemampuan dasar (makan, tidur, berjalan)

ANAK (Child Class):
- Mewarisi sifat orang tua
- Punya sifat tambahan sendiri (bakat musik, olahraga)
- Bisa pakai kemampuan orang tua
- Bisa override kemampuan (cara tidur beda)

Visualisasi Keluarga:
         BINATANG
        ╱    │    ╲
     ANJING  KUCING  BURUNG
      │       │       │
   Guk guk  Meow   Cuit cuit
```

---

### POLYMORPHISM - Restoran All-You-Can-Eat

```
Bayangkan polymorphism seperti menu all-you-can-eat:

MENU UMUM: "Ambil makanan"

TAPI:
- Pizza diambil dari oven
- Sup diambil dari panci
- Salad diambil dari bowl

ANALOGI:
- Semua adalah "makanan"
- Tapi cara ambilnya berbeda
- Caller tidak perlu tahu detailnya

Visualisasi:
      MAKANAN (Parent)
        │
        ├─ Pizza.ambil()    → Dari oven
        ├─ Sup.ambil()      → Dari panci
        └─ Salad.ambil()    → Dari bowl

Kode:
def ambil_makanan(makanan):
    makanan.ambil()  # Bisa pizza, sup, salad - cara ambilnya beda
```

---

### ENCAPSULATION - Kotak Hadiah Tertutup

```
Bayangkan encapsulation seperti kotak hadiah:

PUBLIK (bisa dilihat):
- Sisi luar kotak (bisa dilihat semua orang)

PRIVATE (tidak boleh dibuka):
- Isi kotak (hanya pemberi tahu yang tahu)
- Jika mau lihat isi → minta ke pemberi tahu

ANALOGI:
- Kotak hadiah tidak boleh dibuka sembarangan
- Harus bertanya ke pemilik
- Pemilik bisa tentukan apa yang boleh diambil

Kode:
class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo  # Private - dengan __ di depan
    
    def get_saldo(self):      # Public method untuk akses
        return self.__saldo
    
    def setor(self, jumlah):  # Public method untuk ubah
        if jumlah > 0:
            self.__saldo += jumlah

Visualisasi:
  ┌──────────────────────┐
  │   PUBLIC INTERFACE   │  ← Orang bisa akses
  │  get_saldo()         │
  │  setor(jumlah)       │
  │                      │
  │  ┌────────────────┐  │
  │  │ PRIVATE DATA   │  │  ← Orang tidak bisa
  │  │ __saldo        │  │     akses langsung
  │  └────────────────┘  │
  │                      │
  └──────────────────────┘
```

---

### ABSTRACTION - Mobil Otomatis

```
Bayangkan abstraction seperti mobil otomatis:

TAMPILAN LUAR:
- Kemudi, pedal gas, pedal rem
- Sederhana untuk digunakan

INSIDE ENGINE:
- Kompleks! Piston, silinder, carburator
- User tidak perlu tahu detailnya

Analogi:
- User hanya tahu: gas → mobil jalan
- User tidak perlu tahu: bagaimana engine bekerja
- Interface simple, implementasi kompleks

Kode:
class Mobil:
    def percepat(self):       # Interface simple
        self._kompres_fuel()  # Kompleks di dalam
        self._bakar_fuel()
        self._dorong_piston()
    
    def _kompres_fuel(self):  # Private (dengan _)
        # Logika kompleks...
        pass
```

---

## 💡 Mengapa Penting?

### Alasan untuk OOP

| Konsep | Alasan Penting |
|---|---|
| **Class** | Organize kode dengan struktur yang jelas |
| **Inheritance** | Reuse kode, mengurangi duplikasi |
| **Polymorphism** | Fleksibilitas, mudah tambah fitur baru |
| **Encapsulation** | Keamanan data, interface yang jelas |
| **Abstraction** | Sembunyikan kompleksitas, user-friendly |

---

## ✅ Kapan Digunakan?

| Konsep | Kapan Digunakan |
|---|---|
| **Class** | Program lebih dari 500 baris, data kompleks |
| **Inheritance** | Ada persamaan antara class-class |
| **Polymorphism** | Banyak class dengan method yang sama |
| **Encapsulation** | Data sensitif yang tidak boleh diubah sembarangan |
| **Abstraction** | Logika kompleks yang user tidak perlu tahu |

---

## 📌 Kode Contoh

### CLASS - Membuat Objek Siswa

```python
class Siswa:
    def __init__(self, nama, nis, nilai):
        self.nama = nama
        self.nis = nis
        self.nilai = nilai
    
    def cetak_data(self):
        print(f"Nama: {self.nama}, NIS: {self.nis}, Nilai: {self.nilai}")
    
    def lulus(self):
        return self.nilai >= 60

# Membuat object
siswa1 = Siswa("Ari", "001", 80)
siswa2 = Siswa("Budi", "002", 55)

siswa1.cetak_data()  # Nama: Ari, NIS: 001, Nilai: 80
print(siswa1.lulus())  # True
print(siswa2.lulus())  # False
```

### INHERITANCE - Menurun dari Parent Class

```python
# Parent class
class Hewan:
    def __init__(self, nama):
        self.nama = nama
    
    def suara(self):
        print("Suara umum")

# Child class
class Anjing(Hewan):
    def suara(self):      # Override method
        print(f"{self.nama} bersuara: Guk guk!")

class Kucing(Hewan):
    def suara(self):      # Override method
        print(f"{self.nama} bersuara: Meow meow!")

# Gunakan
anjing = Anjing("Rex")
kucing = Kucing("Mimi")

anjing.suara()   # Rex bersuara: Guk guk!
kucing.suara()   # Mimi bersuara: Meow meow!
```

### POLYMORPHISM - Method Sama, Behavior Beda

```python
def buat_suara(hewan):
    hewan.suara()  # Bisa anjing, kucing, atau hewan lain

# Gunakan dengan berbagai object
hewan_list = [
    Anjing("Rex"),
    Kucing("Mimi"),
    Hewan("Binatang")
]

for hewan in hewan_list:
    buat_suara(hewan)  # Setiap object punya behavior berbeda
```

### ENCAPSULATION - Private Data

```python
class BankAccount:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = saldo_awal  # Private
    
    def get_saldo(self):
        return self.__saldo
    
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor {jumlah}. Saldo baru: {self.__saldo}")
        else:
            print("Jumlah harus positif!")
    
    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Tarik {jumlah}. Saldo baru: {self.__saldo}")
        else:
            print("Saldo tidak cukup!")

# Gunakan
akun = BankAccount("Ari", 1000)
akun.setor(500)         # Setor 500. Saldo baru: 1500
akun.tarik(200)         # Tarik 200. Saldo baru: 1300
print(akun.get_saldo()) # 1300

# Tidak bisa akses langsung
# print(akun.__saldo)   ← ERROR! Private
```

---

## 🎓 Ringkasan Fase 6

| Aspek | Penjelasan |
|---|---|
| **Class** | Blueprint untuk membuat object |
| **Inheritance** | Child class mewarisi dari parent class |
| **Polymorphism** | Method sama, behavior berbeda |
| **Encapsulation** | Hide private data, expose public interface |
| **Abstraction** | Sembunyikan kompleksitas |

---

## 🚀 Lanjut ke Fase 7

Setelah menguasai OOP, fase berikutnya adalah **Real-World Projects** - menggabungkan semua skill untuk membuat aplikasi nyata.

👉 **Baca:** `16_TEORI_PROJECT.md`  
👉 **Kode:** `07_oop_exercise.py` atau `08_ringkasan_pembelajaran.py`

---

*Versi: 1.0 | Last Updated: 2026-04-10*
