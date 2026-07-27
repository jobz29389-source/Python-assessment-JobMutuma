"""Task 3: Python Data Types"""

# a. Integer
age = 21
print(age, type(age))

# b. Float
price = 49.99
print(price * 2)

# c. Boolean
is_active = True
if is_active:
    print("Account is active")

# d. String
name = "Job" + " Mutuma"
print(name[:2], len(name))

# e. List
fruits = ["apple", "banana", "mango", "grape", "kiwi"]
fruits.append("orange")
fruits.remove("banana")
print(fruits[0], fruits)

# f. Tuple (immutable)
coordinates = (1, 2, 3)
try:
    coordinates[0] = 99
except TypeError as e:
    print("Error:", e)

# g. Set
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)

# h. Dictionary
student = {"name": "Job", "age": 21, "course": "IT"}
print(student["name"])
student["year"] = 2
del student["age"]
print(student)

# i. Type casting
num_str = "10"
num_int = int(num_str)
num_float = float(num_int)
back_to_str = str(num_float)
print(num_int, num_float, back_to_str, type(back_to_str))