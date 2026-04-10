# 1. Mengambil input dari user
# Ingat : Hasil input() selalu bertipe string (teks)
nama_pembeli    = input("Masukkan nama pembeli : ")
jumlah_bakso    = input("Berapa mangkok bakso : ")

# 2. Konversi tipe data (Casting)
# karena jumlah_bakso itu angka, kita harus ubah dari String ke Ineger (int)
jumlah_baks0 = int(jumlah_bakso)

# 3. Menghitung total ( Operator Aritmatika : *)
harga_permangkok = 15000
total_bayar = jumlah_baks0 * harga_permangkok

# 4. Outputyang keren (f-string)
print(f"\nHalo {nama_pembeli} !")
print(f"Total yang harus dibayar untuk {jumlah_baks0} bakso adalah : Rp. {total_bayar}")