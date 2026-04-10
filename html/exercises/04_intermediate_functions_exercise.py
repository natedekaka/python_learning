#!/usr/bin/env python3
"""
Intermediate - Exercise 2: Functions & Strings
===============================================

SOAL:
1. Buat function untuk menghitung BMI
2. Buat function untuk check string palindrome
3. Buat function untuk reverse string
4. Buat function dengan multiple return values
5. Buat function dengan default parameters
"""

# ===== SOAL 1: Function BMI =====
print("=" * 50)
print("SOAL 1: Hitung BMI")
print("=" * 50)

def hitung_bmi(berat, tinggi):
    """
    Fungsi untuk menghitung BMI
    Rumus: BMI = berat (kg) / (tinggi (m))^2
    """
    bmi = berat / (tinggi ** 2)
    return bmi

def kategori_bmi(bmi):
    """Tentukan kategori BMI"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

berat = 70  # kg
tinggi = 1.75  # m
bmi_value = hitung_bmi(berat, tinggi)
kategori = kategori_bmi(bmi_value)

print(f"Berat: {berat} kg, Tinggi: {tinggi} m")
print(f"BMI: {bmi_value:.2f}")
print(f"Kategori: {kategori}")

# ===== SOAL 2: Palindrome Check =====
print("\n" + "=" * 50)
print("SOAL 2: Cek Palindrome")
print("=" * 50)

def adalah_palindrome(text):
    """Check apakah string adalah palindrome"""
    text_clean = text.lower().replace(" ", "")
    return text_clean == text_clean[::-1]

words = ["racecar", "hello", "a man a plan a canal panama"]
for word in words:
    hasil = adalah_palindrome(word)
    print(f"'{word}': {hasil}")

# ===== SOAL 3: Reverse String =====
print("\n" + "=" * 50)
print("SOAL 3: Reverse String")
print("=" * 50)

def reverse_string(text):
    """Reverse sebuah string"""
    return text[::-1]

def reverse_string_v2(text):
    """Reverse dengan loop"""
    result = ""
    for char in text:
        result = char + result
    return result

text = "Python"
print(f"Original: {text}")
print(f"Reversed (slice): {reverse_string(text)}")
print(f"Reversed (loop): {reverse_string_v2(text)}")

# ===== SOAL 4: Multiple Return Values =====
print("\n" + "=" * 50)
print("SOAL 4: Multiple Return Values")
print("=" * 50)

def analisis_nilai(nilai_list):
    """Return multiple values: min, max, average"""
    minimum = min(nilai_list)
    maximum = max(nilai_list)
    average = sum(nilai_list) / len(nilai_list)
    return minimum, maximum, average

nilai = [85, 90, 78, 95, 88]
min_val, max_val, avg_val = analisis_nilai(nilai)

print(f"Nilai: {nilai}")
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val:.2f}")

# ===== SOAL 5: Default Parameters =====
print("\n" + "=" * 50)
print("SOAL 5: Default Parameters")
print("=" * 50)

def greet(nama, greeting="Hello", punctuation="!"):
    """Greet dengan default parameters"""
    return f"{greeting}, {nama}{punctuation}"

print(greet("Ari"))
print(greet("Budi", greeting="Hi"))
print(greet("Citra", greeting="Good morning", punctuation="!!!"))

print("\n✅ Latihan Selesai!")
