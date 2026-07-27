"""Task 5: Functions in Python"""

# a. Built-in functions
nums = [4, 1, 7, 3]
print(len(nums), max(nums), sorted(nums))

# b. User-defined function
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 3))

# c. Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Job"))
print(greet("Job", "Hi"))

# d. *args
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))

# e. Lambda + map
square = lambda x: x ** 2
squared_nums = list(map(square, nums))
print(squared_nums)

# f. Scope: local vs global
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)