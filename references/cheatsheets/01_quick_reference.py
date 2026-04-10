#!/usr/bin/env python3
"""
QUICK REFERENCE - PYTHON CHEAT SHEET
=====================================
File: quick_reference.py
Gunakan untuk cepat mencari syntax dan contoh code
"""

print("=" * 60)
print("PYTHON QUICK REFERENCE CHEAT SHEET")
print("=" * 60)

# ===== 1. DATA TYPES =====
print("\n1️⃣  DATA TYPES")
print("-" * 60)

# String
text = "Hello"
print(f"String: {text}, Type: {type(text)}")
print(f"  Methods: .upper(), .lower(), .split(), .replace(), .strip()")

# Integer & Float
num_int = 10
num_float = 10.5
print(f"Integer: {num_int}, Float: {num_float}")

# Boolean
is_valid = True
print(f"Boolean: {is_valid}, Negation: {not is_valid}")

# List (ordered, mutable)
my_list = [1, 2, 3]
print(f"List: {my_list}, Methods: .append(), .remove(), .pop(), .sort()")

# Tuple (ordered, immutable)
my_tuple = (1, 2, 3)
print(f"Tuple: {my_tuple}")

# Dictionary (key-value)
my_dict = {"name": "Ari", "age": 25}
print(f"Dict: {my_dict}")

# Set (unique, unordered)
my_set = {1, 2, 3}
print(f"Set: {my_set}")

# ===== 2. OPERATORS =====
print("\n2️⃣  OPERATORS")
print("-" * 60)

print("Arithmetic: +, -, *, /, //, %, **")
print(f"  10 / 3 = {10 / 3} (float division)")
print(f"  10 // 3 = {10 // 3} (integer division)")
print(f"  10 ** 3 = {10 ** 3} (power)")

print("\nComparison: ==, !=, <, >, <=, >=")
print(f"  5 == 5: {5 == 5}")
print(f"  5 != 3: {5 != 3}")

print("\nLogical: and, or, not")
print(f"  True and False: {True and False}")
print(f"  True or False: {True or False}")

# ===== 3. STRINGS =====
print("\n3️⃣  STRINGS")
print("-" * 60)

name = "Ari"
age = 25

# f-string (recommended)
print(f"F-string: Name={name}, Age={age}")

# format() method
print("format(): Name={}, Age={}".format(name, age))

# % operator
print("%% operator: Name=%s, Age=%d" % (name, age))

# String methods
print("Methods: .upper(), .lower(), .title(), .capitalize()")
print(f"  'hello'.upper() = {'hello'.upper()}")
print(f"  'HELLO'.lower() = {'HELLO'.lower()}")

# ===== 4. LISTS =====
print("\n4️⃣  LISTS")
print("-" * 60)

items = [1, 2, 3, 4, 5]
print(f"List: {items}")
print(f"  Length: len(items) = {len(items)}")
print(f"  First: items[0] = {items[0]}")
print(f"  Last: items[-1] = {items[-1]}")
print(f"  Slice: items[1:3] = {items[1:3]}")
print(f"  Sum: sum(items) = {sum(items)}")
print(f"  Max: max(items) = {max(items)}")
print(f"  Min: min(items) = {min(items)}")

# List methods
lst = [3, 1, 4, 1, 5]
lst.append(9)
lst.sort()
print(f"  After append & sort: {lst}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"  Comprehension [x**2 for x in range(5)]: {squares}")

# ===== 5. DICTIONARIES =====
print("\n5️⃣  DICTIONARIES")
print("-" * 60)

person = {"name": "Ari", "age": 25, "city": "Jakarta"}
print(f"Dict: {person}")
print(f"  Get: person['name'] = {person['name']}")
print(f"  Get with default: person.get('job', 'N/A') = {person.get('job', 'N/A')}")
print(f"  Keys: person.keys() = {person.keys()}")
print(f"  Values: person.values() = {person.values()}")
print(f"  Items: person.items() = {person.items()}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 4)}
print(f"  Comprehension: {squares_dict}")

# ===== 6. CONTROL FLOW =====
print("\n6️⃣  CONTROL FLOW")
print("-" * 60)

print("If/Elif/Else:")
value = 75
if value >= 90:
    result = "A"
elif value >= 80:
    result = "B"
else:
    result = "C"
print(f"  Value {value} -> Grade {result}")

print("\nFor Loop:")
print("  for i in range(3): print(i)")
for i in range(3):
    print(f"    {i}")

print("\nWhile Loop:")
print("  count = 0; while count < 3: print(count); count += 1")
count = 0
while count < 3:
    print(f"    {count}")
    count += 1

print("\nFor with enumerate:")
for i, val in enumerate(['a', 'b', 'c']):
    print(f"    {i}: {val}")

# ===== 7. FUNCTIONS =====
print("\n7️⃣  FUNCTIONS")
print("-" * 60)

def greet(name, greeting="Hello"):
    """Simple greeting function"""
    return f"{greeting}, {name}!"

print(f"Basic function: greet('Ari') = {greet('Ari')}")
print(f"With default param: greet('Ari', 'Hi') = {greet('Ari', 'Hi')}")

def multiple_return(x):
    """Function dengan multiple return"""
    return x * 2, x * 3

result1, result2 = multiple_return(5)
print(f"Multiple return: {result1}, {result2}")

# Lambda
square = lambda x: x ** 2
print(f"Lambda: lambda x: x**2, square(5) = {square(5)}")

# Map & Filter
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Map (x*2): {doubled}")
print(f"Filter (even): {even}")

# ===== 8. CLASSES & OOP =====
print("\n8️⃣  CLASSES & OOP")
print("-" * 60)

class Dog:
    species = "Canis familiaris"  # Class variable
    
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age
    
    def speak(self):
        return f"{self.name} says Woof!"
    
    def __str__(self):
        return f"Dog({self.name}, {self.age})"

dog = Dog("Buddy", 3)
print(f"Create object: dog = Dog('Buddy', 3)")
print(f"  dog.name = {dog.name}")
print(f"  dog.species = {dog.species}")
print(f"  dog.speak() = {dog.speak()}")
print(f"  str(dog) = {str(dog)}")

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

cat = Cat("Whiskers")
print(f"\nInheritance: cat.speak() = {cat.speak()}")

# ===== 9. EXCEPTIONS =====
print("\n9️⃣  EXCEPTIONS")
print("-" * 60)

print("Try/Except:")
try:
    result = 10 / 2
except ZeroDivisionError:
    result = 0
print(f"  10 / 2 = {result}")

try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Error: Cannot divide by zero"
print(f"  10 / 0 = {result}")

print("\nTry/Except/Else/Finally:")
try:
    num = int("abc")
except ValueError:
    print("  ERROR: Invalid integer")
else:
    print(f"  Converted: {num}")
finally:
    print("  Done!")

# ===== 10. FILE I/O =====
print("\n🔟 FILE I/O")
print("-" * 60)

print("Read file:")
print("  with open('file.txt', 'r') as f:")
print("      content = f.read()")

print("\nWrite file:")
print("  with open('file.txt', 'w') as f:")
print("      f.write('Hello')")

print("\nAppend file:")
print("  with open('file.txt', 'a') as f:")
print("      f.write('More text')")

print("\nRead line by line:")
print("  with open('file.txt', 'r') as f:")
print("      for line in f:")
print("          print(line.strip())")

# ===== 11. USEFUL FUNCTIONS =====
print("\n1️⃣1️⃣  USEFUL BUILT-IN FUNCTIONS")
print("-" * 60)

print("Type checking: type(), isinstance()")
print(f"  type(5) = {type(5)}")
print(f"  isinstance(5, int) = {isinstance(5, int)}")

print("\nLength & size: len(), abs()")
print(f"  len([1,2,3]) = {len([1,2,3])}")
print(f"  abs(-10) = {abs(-10)}")

print("\nMin, Max, Sum, Sorted:")
nums = [3, 1, 4, 1, 5, 9]
print(f"  min({nums}) = {min(nums)}")
print(f"  max({nums}) = {max(nums)}")
print(f"  sum({nums}) = {sum(nums)}")
print(f"  sorted({nums}) = {sorted(nums)}")

print("\nRange & Enumerate:")
print(f"  list(range(3)) = {list(range(3))}")
print(f"  list(range(1, 4)) = {list(range(1, 4))}")
print(f"  list(enumerate(['a','b'])) = {list(enumerate(['a','b']))}")

print("\nZip:")
names = ['a', 'b', 'c']
ages = [25, 30, 35]
print(f"  list(zip({names}, {ages})) = {list(zip(names, ages))}")

print("\nMap & Filter:")
print(f"  list(map(str.upper, ['a','b'])) = {list(map(str.upper, ['a','b']))}")
print(f"  list(filter(lambda x: x>2, [1,2,3])) = {list(filter(lambda x: x>2, [1,2,3]))}")

# ===== 12. STRING METHODS =====
print("\n1️⃣2️⃣  STRING METHODS REFERENCE")
print("-" * 60)

text = "  Hello World  "
print(f"Original: '{text}'")
print(f"  .strip() = '{text.strip()}'")
print(f"  .upper() = '{text.upper()}'")
print(f"  .lower() = '{text.lower()}'")
print(f"  .replace('World', 'Python') = '{text.replace('World', 'Python')}'")
print(f"  .split() = {text.split()}")
print(f"  .startswith('  H') = {text.startswith('  H')}")
print(f"  .endswith('d  ') = {text.endswith('d  ')}")
print(f"  .find('World') = {text.find('World')}")
print(f"  .count('l') = {text.count('l')}")

# ===== 13. TIPS & TRICKS =====
print("\n1️⃣3️⃣  TIPS & TRICKS")
print("-" * 60)

print("1. Multiple assignment:")
a, b = 1, 2
print(f"   a, b = 1, 2 -> a={a}, b={b}")

print("\n2. Swapping variables:")
a, b = b, a
print(f"   a, b = b, a -> a={a}, b={b}")

print("\n3. Unpacking:")
coords = (10, 20)
x, y = coords
print(f"   coords = {coords} -> x={x}, y={y}")

print("\n4. Ternary operator:")
age = 25
status = "Adult" if age >= 18 else "Minor"
print(f"   'Adult' if age >= 18 else 'Minor' -> {status}")

print("\n5. Membership checking:")
lst = [1, 2, 3]
print(f"   2 in [1,2,3] -> {2 in lst}")
print(f"   5 not in [1,2,3] -> {5 not in lst}")

print("\n6. Dictionary get with default:")
data = {"name": "Ari"}
print(f"   data.get('age', 25) -> {data.get('age', 25)}")

print("\n7. F-string formatting:")
price = 19.5
print(f"   f'Price: ${{price:.2f}}' -> f'Price: ${price:.2f}'")

# ===== SELESAI =====
print("\n" + "=" * 60)
print("✅ QUICK REFERENCE COMPLETE!")
print("Untuk contoh lebih lengkap, lihat file pembelajaran lainnya")
print("=" * 60)
