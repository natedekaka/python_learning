# Python Quick Reference Cheat Sheet

## 1️⃣ DATA TYPES

### String
- Methods: `.upper()`, `.lower()`, `.split()`, `.replace()`, `.strip()`
- Example: `text = "Hello"`, `text.upper()` → `"HELLO"`

### Integer & Float
- Integer: `num_int = 10`
- Float: `num_float = 10.5`

### Boolean
- Values: `True` or `False`
- Negation: `not is_valid`

### Lists
```python
my_list = [1, 2, 3, 4]
my_list.append(5)
my_list[0]  # Akses elemen pertama
```

### Dictionaries
```python
my_dict = {"name": "John", "age": 25}
my_dict["name"]  # Akses value
```

## 2️⃣ OPERATORS

### Arithmetic
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Floor Division: `//`
- Modulo: `%`
- Power: `**`

### Comparison
- `==` (equal), `!=` (not equal)
- `<` (less than), `>` (greater than)
- `<=` (less or equal), `>=` (greater or equal)

### Logical
- `and`: Both conditions must be True
- `or`: One condition must be True
- `not`: Negate condition

## 3️⃣ CONTROL FLOW

### If-Else
```python
if condition:
    # Do something
elif other_condition:
    # Do other thing
else:
    # Do default
```

### Loops
```python
# For loop
for i in range(10):
    print(i)

# While loop
while condition:
    # Do something
    if stop_condition:
        break
```

## 4️⃣ FUNCTIONS
```python
def my_function(param1, param2):
    """Docstring untuk menjelaskan fungsi"""
    return param1 + param2
```

## 5️⃣ COMMON METHODS
- `len()`: Get length
- `range()`: Generate sequence
- `type()`: Get data type
- `print()`: Print to console
- `input()`: Get user input
- `int()`, `str()`, `float()`: Type conversion

---
📚 For more details, see `references/theory/`
