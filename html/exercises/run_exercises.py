#!/usr/bin/env python3
"""
Python Learning Repository - Exercise Menu
===========================================

Program interaktif untuk menjalankan semua exercises dengan mudah.
"""

import os
import subprocess
import sys
from pathlib import Path

# Define exercises
EXERCISES = {
    "1": {
        "name": "Variables & Data Types",
        "file": "01_fundamentals_exercise.py",
        "level": "Fundamentals",
        "description": "Deklarasi variables, type checking, operasi arithmetic"
    },
    "2": {
        "name": "Input & Calculation",
        "file": "02_fundamentals_input_exercise.py",
        "level": "Fundamentals",
        "description": "User input, kalkulasi nilai, if/else logic"
    },
    "3": {
        "name": "Loops & Conditions",
        "file": "03_intermediate_loops_exercise.py",
        "level": "Intermediate",
        "description": "For loops, while loops, nested loops, patterns"
    },
    "4": {
        "name": "Functions & Strings",
        "file": "04_intermediate_functions_exercise.py",
        "level": "Intermediate",
        "description": "Function definition, string methods, palindrome check"
    },
    "5": {
        "name": "Files & Exceptions",
        "file": "05_intermediate_files_exercise.py",
        "level": "Intermediate",
        "description": "File I/O, try/except, error handling"
    },
    "6": {
        "name": "OOP & Classes",
        "file": "06_advanced_oop_exercise.py",
        "level": "Advanced",
        "description": "Classes, inheritance, polymorphism, methods"
    }
}

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Print main menu"""
    clear_screen()
    print("=" * 60)
    print("🐍 Python Learning Repository - Exercise Menu")
    print("=" * 60)
    print()
    
    current_level = None
    for key, exercise in EXERCISES.items():
        level = exercise["level"]
        if level != current_level:
            print(f"\n{level.upper()}")
            print("-" * 60)
            current_level = level
        
        print(f"  [{key}] {exercise['name']}")
        print(f"      {exercise['description']}")
    
    print()
    print("-" * 60)
    print("  [L] List all exercises (detailed)")
    print("  [V] View exercise file")
    print("  [Q] Quit")
    print("=" * 60)

def print_detailed_list():
    """Print detailed list of all exercises"""
    clear_screen()
    print("=" * 60)
    print("📚 DETAILED EXERCISE LIST")
    print("=" * 60)
    print()
    
    current_level = None
    for key, exercise in EXERCISES.items():
        level = exercise["level"]
        if level != current_level:
            print(f"\n{'🟢 FUNDAMENTALS' if level == 'Fundamentals' else '🟡 INTERMEDIATE' if level == 'Intermediate' else '🔴 ADVANCED'}")
            print("-" * 60)
            current_level = level
        
        print(f"\nExercise {key}: {exercise['name']}")
        print(f"File: {exercise['file']}")
        print(f"Description: {exercise['description']}")
    
    print("\n" + "=" * 60)
    input("\nPress Enter to continue...")

def run_exercise(exercise_num):
    """Run selected exercise"""
    if exercise_num not in EXERCISES:
        print("❌ Nomor exercise tidak valid!")
        input("Press Enter to continue...")
        return
    
    exercise = EXERCISES[exercise_num]
    file_path = Path(__file__).parent / exercise["file"]
    
    if not file_path.exists():
        print(f"❌ File tidak ditemukan: {file_path}")
        input("Press Enter to continue...")
        return
    
    clear_screen()
    print("=" * 60)
    print(f"▶️  Running: {exercise['name']}")
    print("=" * 60)
    print()
    
    try:
        subprocess.run([sys.executable, str(file_path)])
    except KeyboardInterrupt:
        print("\n\n⏹️  Program dihentikan oleh user")
    except Exception as e:
        print(f"❌ Error saat menjalankan file: {e}")
    
    print()
    input("Press Enter untuk kembali ke menu...")

def view_exercise_code(exercise_num):
    """View exercise file content"""
    if exercise_num not in EXERCISES:
        print("❌ Nomor exercise tidak valid!")
        input("Press Enter to continue...")
        return
    
    exercise = EXERCISES[exercise_num]
    file_path = Path(__file__).parent / exercise["file"]
    
    if not file_path.exists():
        print(f"❌ File tidak ditemukan: {file_path}")
        input("Press Enter to continue...")
        return
    
    clear_screen()
    print("=" * 60)
    print(f"📄 File: {exercise['file']}")
    print("=" * 60)
    print()
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        print(content)
    except Exception as e:
        print(f"❌ Error saat membaca file: {e}")
    
    print()
    input("Press Enter untuk kembali ke menu...")

def main():
    """Main menu loop"""
    while True:
        print_menu()
        choice = input("Pilih nomor exercise atau perintah [1-6/L/V/Q]: ").strip().upper()
        
        if choice == "Q":
            print("\n👋 Terima kasih sudah belajar! Sampai jumpa!")
            break
        elif choice == "L":
            print_detailed_list()
        elif choice == "V":
            num = input("\nMasukkan nomor exercise untuk dilihat [1-6]: ").strip()
            view_exercise_code(num)
        elif choice in EXERCISES:
            run_exercise(choice)
        else:
            print("❌ Pilihan tidak valid!")
            input("Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan!")
        sys.exit(0)
