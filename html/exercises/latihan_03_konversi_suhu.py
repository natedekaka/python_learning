#!/usr/bin/env python3
"""
==========================================
LATIHAN 3: KONVERSI SUUHU
==========================================
Tujuan: Memahami operator aritmatika dengan formula nyata

Konsep yang dipelajari:
- Input user (input())
- Type conversion (int(), float())
- Operator aritmatika
- Formula matematika

==========================================
"""

print("=" * 50)
print("🌡️ KONVERSI SUHU")
print("=" * 50)

# ==============================
# CELSIUS KE SATUAN LAIN
# ==============================

print("\n📌 KONVERSI DARI CELSIUS")
print("-" * 50)

# TODO 1: Input suhu dalam Celsius
celsius = float(input("Masukkan suhu (°C): "))

# TODO 2: Konversi ke Fahrenheit
# Formula: F = (C × 9/5) + 32
fahrenheit = ...
print(f"\n🌡️  {celsius}°C = {fahrenheit}°F")

# TODO 3: Konversi ke Kelvin
# Formula: K = C + 273.15
kelvin = ...
print(f"🌡️  {celsius}°C = {kelvin}K")

# TODO 4: Konversi ke Reamur
# Formula: R = C × 4/5
reamur = ...
print(f"🌡️  {celsius}°C = {reamur}°R")

# ==============================
# FAHRENHEIT KE SATUAN LAIN
# ==============================

print("\n📌 KONVERSI DARI FAHRENHEIT")
print("-" * 50)

# TODO 5: Input suhu dalam Fahrenheit
fahrenheit_input = float(input("Masukkan suhu (°F): "))

# Konversi ke Celsius
# Formula: C = (F - 32) × 5/9
celsius_dari_f = ...
print(f"\n🌡️  {fahrenheit_input}°F = {celsius_dari_f}°C")

# Konversi ke Kelvin
# Formula: K = (F - 32) × 5/9 + 273.15
kelvin_dari_f = ...
print(f"🌡️  {fahrenheit_input}°F = {kelvin_dari_f}K")

# ==============================
# TABEL PERBANDINGAN SUHU
# ==============================

print("\n" + "=" * 50)
print("📊 TABEL SUHU (Dari 0°C - 100°C)")
print("=" * 50)
print(f"{'°C':>6} | {'°F':>6} | {'K':>6} | {'°R':>6}")
print("-" * 35)

# TODO 6: Buat tabel suhu dari 0, 25, 50, 75, 100
suhu_c = [0, 25, 50, 75, 100]

for c in suhu_c:
    # Hitung semua konversi
    f = (c * 9/5) + 32
    k = c + 273.15
    r = c * 4/5
    
    print(f"{c:>6} | {f:>6.1f} | {k:>6.1f} | {r:>6.1f}")

# ==============================
# PROGRAM INTERAKTIF
# ==============================

print("\n" + "=" * 50)
print("🎮 PROGRAM SUHU INTERAKTIF")
print("=" * 50)

def konversi_suhu():
    """Fungsi utama konversi suhu"""
    
    print("\nPilih konversi:")
    print("1. Celsius → Fahrenheit")
    print("2. Celsius → Kelvin")
    print("3. Fahrenheit → Celsius")
    print("4. Kelvin → Celsius")
    print("5. Keluar")
    
    pilihan = input("\nMasukkan pilihan (1-5): ")
    
    if pilihan == "1":
        c = float(input("Masukkan suhu °C: "))
        f = (c * 9/5) + 32
        print(f"\n✅ Hasil: {c}°C = {f}°F")
        
    elif pilihan == "2":
        c = float(input("Masukkan suhu °C: "))
        k = c + 273.15
        print(f"\n✅ Hasil: {c}°C = {k}K")
        
    elif pilihan == "3":
        f = float(input("Masukkan suhu °F: "))
        c = (f - 32) * 5/9
        print(f"\n✅ Hasil: {f}°F = {c}°C")
        
    elif pilihan == "4":
        k = float(input("Masukkan suhu K: "))
        c = k - 273.15
        print(f"\n✅ Hasil: {k}K = {c}°C")
        
    elif pilihan == "5":
        print("\n👋 Terima kasih!")
        return False
    
    else:
        print("\n❌ Pilihan tidak valid!")
    
    return True

# Jalankan program
while True:
    if not konversi_suhu():
        break

print("\n✅ Latihan 3 Selesai!")
