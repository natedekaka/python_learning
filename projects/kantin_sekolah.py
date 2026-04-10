harga_jajanan = [2000, 5000, 1500, 3000, 10000]

total_bayar = 0

print("--- STRUK KAMTIN KEJUJURAN ---")

for harga in harga_jajanan:
    total_bayar = total_bayar + harga
    print(f"Item harga : Rp {harga} -> Total sementara : Rp. {total_bayar}")

print("-------------------------------")
print(f"TOTAL YANG HARUS DIBAYAR : Rp. {total_bayar}")

if total_bayar > 2000:
    print("selamat ! kamu dapat Bonus 1 gelas teh manis")