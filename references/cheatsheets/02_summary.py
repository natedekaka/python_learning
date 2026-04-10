#!/usr/bin/env python3
"""
RINGKASAN PEMBELAJARAN PYTHON
==============================
Path: /home/daniarsyah/projects/python/python_learning
Created: 2026-04-10

Progress: 7 file pembelajaran + 1 exercise telah selesai ✅
"""

print("=" * 60)
print("RINGKASAN PEMBELAJARAN PYTHON")
print("=" * 60)

learning_path = [
    {
        "fase": 1,
        "file": "01_basics.py",
        "topik": "VARIABLES & DATA TYPES",
        "materi": [
            "String, Integer, Float, Boolean",
            "Lists, Dictionaries",
            "Basic Operations (+, -, *, /, //, %, **)"
        ],
        "status": "✅ SELESAI"
    },
    {
        "fase": 2,
        "file": "02_latihan.py",
        "topik": "PRACTICE: DATA & INFO DIRI",
        "materi": [
            "List operations (sum, max, min, len)",
            "Dictionary manipulation",
            "String formatting dengan f-string"
        ],
        "status": "✅ SELESAI (Bug Fixed)"
    },
    {
        "fase": 3,
        "file": "03_loops_conditions.py",
        "topik": "LOOPS & CONDITIONS",
        "materi": [
            "if/elif/else statements",
            "for loops & range()",
            "while loops",
            "break & continue",
            "Nested loops"
        ],
        "status": "✅ SELESAI"
    },
    {
        "fase": 4,
        "file": "04_functions_strings.py",
        "topik": "FUNCTIONS & STRING OPERATIONS",
        "materi": [
            "Function definition & parameters",
            "Default parameters & return values",
            "String methods (upper, lower, split, replace, etc)",
            "List & Dictionary comprehension",
            "*args & **kwargs",
            "Lambda functions & map/filter"
        ],
        "status": "✅ SELESAI"
    },
    {
        "fase": 5,
        "file": "05_files_exceptions.py",
        "topik": "FILE OPERATIONS & EXCEPTIONS",
        "materi": [
            "try/except/else/finally",
            "Custom exceptions",
            "File I/O (read, write, append)",
            "Working with CSV & JSON",
            "os module untuk file management"
        ],
        "status": "✅ SELESAI"
    },
    {
        "fase": 6,
        "file": "06_oop.py",
        "topik": "OBJECT-ORIENTED PROGRAMMING",
        "materi": [
            "Classes & Objects",
            "Inheritance & super()",
            "Polymorphism",
            "Encapsulation & Private variables",
            "Class methods & Static methods",
            "Property decorators",
            "Composition vs Inheritance",
            "Multiple inheritance"
        ],
        "status": "✅ SELESAI"
    },
    {
        "fase": 7,
        "file": "07_oop_exercise.py",
        "topik": "PRACTICE: LIBRARY MANAGEMENT SYSTEM",
        "materi": [
            "Menggabungkan konsep OOP",
            "Class design & relationships",
            "State management dalam objects",
            "Real-world problem solving"
        ],
        "status": "✅ SELESAI"
    }
]

# Display learning path
for item in learning_path:
    print(f"\n📚 FASE {item['fase']}: {item['topik']}")
    print(f"   File: {item['file']}")
    print(f"   Status: {item['status']}")
    print(f"   Materi:")
    for materi in item['materi']:
        print(f"      • {materi}")

# ===== SKILL SUMMARY =====
print("\n" + "=" * 60)
print("SKILL SUMMARY")
print("=" * 60)

skills = {
    "FUNDAMENTAL": [
        "✓ Variables & Data Types",
        "✓ Lists & Dictionaries",
        "✓ String manipulation",
        "✓ Basic arithmetic & logic"
    ],
    "CONTROL FLOW": [
        "✓ if/elif/else conditions",
        "✓ for & while loops",
        "✓ break & continue",
        "✓ Nested loops & conditions"
    ],
    "FUNCTIONS": [
        "✓ Function definition & calls",
        "✓ Parameters & return values",
        "✓ *args & **kwargs",
        "✓ Lambda & anonymous functions",
        "✓ map(), filter(), sorted()"
    ],
    "DATA STRUCTURE": [
        "✓ List comprehension",
        "✓ Dictionary comprehension",
        "✓ Tuple operations",
        "✓ Set operations"
    ],
    "FILE & IO": [
        "✓ Read/write files",
        "✓ Work with CSV files",
        "✓ JSON serialization",
        "✓ File system operations"
    ],
    "ERROR HANDLING": [
        "✓ try/except/else/finally",
        "✓ Exception handling",
        "✓ Custom exceptions",
        "✓ Error prevention best practices"
    ],
    "OOP": [
        "✓ Classes & Objects",
        "✓ Inheritance & Polymorphism",
        "✓ Encapsulation & Private variables",
        "✓ Class/Static methods",
        "✓ Composition & Multiple inheritance"
    ]
}

for category, skill_list in skills.items():
    print(f"\n{category}:")
    for skill in skill_list:
        print(f"  {skill}")

# ===== NEXT STEPS =====
print("\n" + "=" * 60)
print("NEXT STEPS - TOPIK YANG BISA DIPELAJARI")
print("=" * 60)

next_topics = {
    "INTERMEDIATE": [
        "Modules & Packages (import, sys, os)",
        "Decorators & Context Managers",
        "Generators & Iterators",
        "Regular Expressions (regex)",
        "Type hints & Documentation",
        "Testing (unittest, pytest)"
    ],
    "LIBRARIES": [
        "NumPy - Numerical computing",
        "Pandas - Data analysis",
        "Matplotlib - Data visualization",
        "Requests - HTTP library",
        "Django/Flask - Web framework"
    ],
    "ADVANCED": [
        "Async/Await Programming",
        "Design Patterns",
        "Performance Optimization",
        "Debugging & Profiling",
        "Database (SQL, SQLAlchemy)",
        "APIs & Web Scraping"
    ],
    "PROJECT IDEAS": [
        "📌 Todo List Application",
        "📌 Contact Manager",
        "📌 Expense Tracker",
        "📌 Weather App (API)",
        "📌 File Organizer Automation",
        "📌 Web Scraper",
        "📌 Chat Application",
        "📌 Game (Pygame)"
    ]
}

for category, topics in next_topics.items():
    print(f"\n{category}:")
    for topic in topics:
        print(f"  → {topic}")

# ===== HOW TO RUN =====
print("\n" + "=" * 60)
print("CARA MENJALANKAN FILE PEMBELAJARAN")
print("=" * 60)

print("""
1. Jalankan satu file:
   $ python3 01_basics.py
   
2. Jalankan semua file:
   $ for file in 0*.py; do echo "\\n=== $file ==="; python3 "$file"; done
   
3. Jalankan file spesifik:
   $ python3 04_functions_strings.py

4. Interaktif mode (REPL):
   $ python3
   >>> from importlib import import_module
   >>> exec(open('01_basics.py').read())
""")

# ===== TIPS & TRICKS =====
print("\n" + "=" * 60)
print("TIPS & BEST PRACTICES")
print("=" * 60)

tips = [
    "💡 Gunakan f-strings untuk formatting (Python 3.6+)",
    "💡 List comprehension lebih cepat dari loop untuk kasus sederhana",
    "💡 Selalu gunakan try/except untuk file operations",
    "💡 Dengan block (with) otomatis menutup file/resources",
    "💡 Gunakan docstrings untuk dokumentasi class & function",
    "💡 Type hints membantu mencegah error: def func(x: int) -> str",
    "💡 PEP 8 adalah style guide resmi Python",
    "💡 Debugging: gunakan print(), pdb.set_trace(), atau debugger IDE"
]

for tip in tips:
    print(f"  {tip}")

# ===== RESOURCES =====
print("\n" + "=" * 60)
print("RESOURCES UNTUK BELAJAR LEBIH LANJUT")
print("=" * 60)

resources = {
    "📖 Official": [
        "Python Official Docs: https://docs.python.org/3/",
        "PEP 8 Style Guide: https://pep8.org/",
        "Python Tutorials: https://docs.python.org/3/tutorial/"
    ],
    "🎓 Learning Platforms": [
        "Codecademy - Interactive Python course",
        "DataCamp - Python for data science",
        "Real Python - In-depth tutorials",
        "W3Schools - Quick reference"
    ],
    "🔧 Tools": [
        "IDE: PyCharm, VS Code, Thonny",
        "REPL: IPython, Jupyter Notebook",
        "Package Manager: pip, conda"
    ]
}

for category, items in resources.items():
    print(f"\n{category}:")
    for item in items:
        print(f"  {item}")

print("\n" + "=" * 60)
print("✅ PEMBELAJARAN BERHASIL!")
print("Terus praktik dan buat project untuk memperdalam skill! 🚀")
print("=" * 60)
