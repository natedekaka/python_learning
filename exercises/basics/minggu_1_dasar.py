# --- Minggu 1: Variabel, Tipe Data, dan List ---

# 1. Variabel
# Variabel adalah wadah untuk menyimpan nilai.
# Gunakan nama yang deskriptif, biasanya dengan format snake_case.

nama_siswa = "Dani"
umur = 17
tinggi_badan = 170.5
is_aktif = True

print(f"Nama: {nama_siswa}, Umur: {umur}, Tinggi: {tinggi_badan}, Aktif: {is_aktif}")


# 2. Tipe Data Dasar
# Python memiliki beberapa tipe data utama:
# - String (teks): "Halo", 'Python'
# - Integer (bilangan bulat): 10, -5
# - Float (bilangan desimal): 3.14, 0.5
# - Boolean (logika): True, False

print("\nTipe data variabel:")
print(f"- nama_siswa: {type(nama_siswa)}")
print(f"- umur: {type(umur)}")
print(f"- tinggi_badan: {type(tinggi_badan)}")
print(f"- is_aktif: {type(is_aktif)}")


# 3. List
# List adalah koleksi item yang berurutan dan bisa diubah (mutable).
# Dibuat dengan kurung siku [ ].

hobi = ["Membaca", "Coding", "Gaming"]

# Mengakses elemen (Index dimulai dari 0)
print(f"\nHobi pertama: {hobi[0]}")
print(f"Hobi terakhir: {hobi[-1]}")

# Menambah item
hobi.append("Musik")
print(f"List hobi setelah ditambah: {hobi}")

# Mengubah item
hobi[1] = "Programming"
print(f"List hobi setelah diubah: {hobi}")

# Menghapus item
hobi.pop(0) # Menghapus berdasarkan index
print(f"List hobi setelah dihapus index 0: {hobi}")


# --- LATIHAN MINGGU 1 ---
# 1. Buat variabel 'nama_sekolah' dan 'jumlah_kelas'.
# 2. Buat list 'mata_pelajaran' yang berisi 3 pelajaran favoritmu.
# 3. Tambahkan 1 pelajaran lagi ke dalam list tersebut.
# 4. Cetak kalimat: "Di sekolah [nama_sekolah] ada [jumlah_kelas] kelas, dan saya suka [mata_pelajaran[0]]."
