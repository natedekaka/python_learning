# --- PROGRAM PERHITUNGAN MATEMATIKA ---
# 1. Deklarasi Variabel & Input (Explicit Casting)
# Kita mengubah inpit (string) menjadi integer secara eksplisit
angka_1 = int(input("Masukkan angka pertama : "))
angka_2 = int(input("Masukkan angka kedua : "))

# 2. Operasi Aritmatika
hasil_tambah = angka_1 + angka_2
hasil_bagi_biasa = angka_1 / angka_2
hasil_bagi_bulat = angka_1 // angka_2
sisa_bagi = angka_1 % angka_2

# 3. Output dengan Teknik f-string
print("\n--- HASIL ANALISIS ---")
print(f"Penjumlahan : {hasil_tambah}")
print(f"Pembagian Float : {hasil_bagi_biasa} (Tipe : {type(hasil_bagi_biasa)})")
print(f"Pembagian Integer (Floor) : {hasil_bagi_bulat}")
print(f"Sisa Hasil Bagi (Modulo) : {sisa_bagi}")

#Contoh Logika Sederhana untuk siswa :
if sisa_bagi == 0:
    print(f"Kesimpulan : {angka_1} habis dibagi oleh {angka_2}")
else:
    print(f"Kesimpulan : {angka_1} tidak habis dibagi oleh {angka_2}")