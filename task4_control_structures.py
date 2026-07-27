"""Task 4: Control Structures - Selection & Looping"""

# a. Grade classifier
marks = 78
if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)

# b. For loop
fruits = ["apple", "banana", "mango", "grape", "kiwi"]
for fruit in fruits:
    print(fruit)

# c. While loop - even numbers 1 to 10
count = 1
while count <= 10:
    if count % 2 == 0:
        print(count)
    count += 1

# d. break and continue
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print("Number:", i)

# e. Nested loop - 3x3 multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()