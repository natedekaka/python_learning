# 📚 Python Learning Journey

Dokumentasi lengkap pembelajaran Python dari dasar hingga OOP dengan praktik nyata.

## 📋 Daftar File Pembelajaran

| # | File | Topik | Status |
|---|------|-------|--------|
| 1 | `01_basics.py` | Variables, Data Types, Operations | ✅ |
| 2 | `02_latihan.py` | Practice: Data & Info Diri | ✅ |
| 3 | `03_loops_conditions.py` | Loops & Conditions | ✅ |
| 4 | `04_functions_strings.py` | Functions & String Operations | ✅ |
| 5 | `05_files_exceptions.py` | File I/O & Exception Handling | ✅ |
| 6 | `06_oop.py` | Object-Oriented Programming | ✅ |
| 7 | `07_oop_exercise.py` | Exercise: Library Management | ✅ |
| 8 | `08_ringkasan_pembelajaran.py` | Complete Summary | ✅ |

## 🎯 Learning Path

### Phase 1: Fundamentals (01-02)
- Variables & data types (string, int, float, bool)
- Lists & Dictionaries
- Basic arithmetic & operations
- **Practice:** Personal data collection

### Phase 2: Control Flow (03)
- if/elif/else statements
- for loops with range()
- while loops
- break & continue
- Nested loops

### Phase 3: Functions & Strings (04)
- Function definition & parameters
- Default parameters & multiple returns
- String methods & formatting
- List & Dictionary comprehension
- *args & **kwargs
- Lambda functions, map, filter

### Phase 4: File I/O & Exceptions (05)
- try/except/else/finally blocks
- Custom exceptions
- Reading & writing files
- CSV & JSON operations
- File system management

### Phase 5: Object-Oriented Programming (06-07)
- Classes & Objects
- Inheritance & Polymorphism
- Encapsulation & Private variables
- Class methods & Static methods
- Composition vs Inheritance
- **Practice:** Library Management System

## 🚀 Quick Start

### Menjalankan file pembelajaran:

```bash
# Jalankan satu file
python3 01_basics.py

# Jalankan file spesifik
python3 04_functions_strings.py

# Jalankan ringkasan pembelajaran
python3 08_ringkasan_pembelajaran.py
```

### Interaktif Mode:

```bash
python3
>>> exec(open('01_basics.py').read())
```

## 💡 Key Concepts Learned

### Fundamental
- ✓ Variables & naming conventions
- ✓ Data types (str, int, float, bool)
- ✓ Collections (list, tuple, dict, set)
- ✓ Type conversion

### Operations & Logic
- ✓ Arithmetic operators (+, -, *, /, //, %, **)
- ✓ Comparison & logical operators
- ✓ String operations & methods
- ✓ List operations & slicing

### Control Flow
- ✓ Conditionals (if/elif/else)
- ✓ Loops (for, while)
- ✓ Loop control (break, continue)
- ✓ Comprehensions (list, dict)

### Functions
- ✓ Function definition & calls
- ✓ Parameters & return values
- ✓ *args & **kwargs
- ✓ Lambda functions
- ✓ Built-in functions (map, filter, sorted)

### File I/O
- ✓ Reading files (read, readline, readlines)
- ✓ Writing files (write, writelines)
- ✓ Appending to files
- ✓ CSV & JSON handling
- ✓ Context managers (with statement)

### Error Handling
- ✓ try/except/else/finally
- ✓ Multiple exception handling
- ✓ Custom exceptions
- ✓ Exception hierarchy

### OOP Concepts
- ✓ Class definition & objects
- ✓ Attributes & methods
- ✓ Constructor (__init__)
- ✓ Inheritance & super()
- ✓ Polymorphism
- ✓ Encapsulation & private variables
- ✓ Class methods & static methods
- ✓ Special methods (__str__, __repr__)
- ✓ Composition & multiple inheritance

## 📖 Topik Lanjutan untuk Dipelajari

### Intermediate
- Modules & Packages
- Decorators
- Context Managers
- Generators & Iterators
- Regular Expressions (regex)
- Type hints
- Unit Testing

### Popular Libraries
- **NumPy** - Numerical computing
- **Pandas** - Data analysis
- **Matplotlib** - Data visualization
- **Requests** - HTTP requests
- **Django/Flask** - Web frameworks
- **Pygame** - Game development

### Advanced Topics
- Async/Await programming
- Design patterns
- Performance optimization
- Debugging & profiling
- Database (SQL, SQLAlchemy)
- Web scraping

## 🎨 Project Ideas

1. **Todo List Application** - Practice: Functions, Lists, File I/O
2. **Contact Manager** - Practice: Dictionaries, File I/O, Search
3. **Expense Tracker** - Practice: OOP, Data structures, Statistics
4. **Weather App** - Practice: APIs, JSON, External libraries
5. **File Organizer** - Practice: File I/O, os module, Automation
6. **Web Scraper** - Practice: Requests, BeautifulSoup, Data processing
7. **Chat Application** - Practice: Sockets, Threading, Data structures
8. **Simple Game** - Practice: Pygame, Game loops, OOP

## 📝 Best Practices

- 💡 Use f-strings for formatting: `f"{variable}"`
- 💡 Use list comprehension for simple transformations
- 💡 Always use try/except for file operations
- 💡 Use `with` statement for file handling (auto-closes)
- 💡 Write docstrings for functions & classes
- 💡 Use type hints: `def func(x: int) -> str:`
- 💡 Follow PEP 8 style guide
- 💡 Debug with print(), pdb, or IDE debugger

## 🔍 Debugging Tips

```python
# Debug dengan print
print(f"Variable: {var}, Type: {type(var)}")

# Debug dengan pdb
import pdb; pdb.set_trace()

# Check type
type(variable)

# Check attributes/methods
dir(object)
help(function)
```

## 📚 Resources

### Official Documentation
- Python Docs: https://docs.python.org/3/
- PEP 8 Style Guide: https://pep8.org/
- Python Tutorial: https://docs.python.org/3/tutorial/

### Learning Platforms
- Real Python: https://realpython.com/
- W3Schools Python: https://www.w3schools.com/python/
- Codecademy: https://www.codecademy.com/

### Tools
- IDE: PyCharm, VS Code (with Python extension), Thonny
- REPL: IPython, Jupyter Notebook
- Package Manager: pip

## ✅ Checklist Pembelajaran

- [x] Phase 1: Variables & Data Types
- [x] Phase 2: Loops & Conditions
- [x] Phase 3: Functions & Strings
- [x] Phase 4: File I/O & Exceptions
- [x] Phase 5: OOP Fundamentals
- [x] Phase 6: OOP Advanced
- [x] Exercise: Library Management System
- [ ] Next: Intermediate Topics
- [ ] Next: Libraries & Frameworks
- [ ] Next: Build Real Projects

## 🎓 Saran Lanjutan

1. **Praktik Konsisten** - Setiap hari kerjakan minimal 1 file
2. **Modifikasi Kode** - Ubah nilai, tambah fitur, eksperimen
3. **Debugging** - Coba buat error dan fix sendiri
4. **Build Projects** - Aplikasikan skill ke project nyata
5. **Read Others' Code** - Belajar dari repository GitHub
6. **Join Communities** - Python Indonesia, Reddit r/learnprogramming
7. **Dokumentasi** - Selalu baca dokumentasi library yang digunakan

## 📞 Kontak & Support

Jika ada pertanyaan atau butuh bantuan:
- Refer ke dokumentasi di setiap file
- Coba jalankan code dan lihat error message
- Gunakan `help()` dan `dir()` di Python REPL
- Search di Python official docs atau StackOverflow

---

**Happy Coding! 🚀**

*Last Updated: 2026-04-10*  
*Learning Path: Dasar → Menengah → Advanced*
