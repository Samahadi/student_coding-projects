"""
Student: Sameer Ahadi
Course: CSC-101
Date: 12/05/2025
Description: File I/O Worksheet
"""

numbers = [45, 78, 102, 56, 89]

file = open("numbers.txt", "w")
for num in numbers:
    file.write(str(num) + "\n")
file.close()

print("Part 1 done: numbers written to numbers.txt")

file = open("numbers.txt", "r")
lines = file.readlines()
file.close()

nums_from_file = []
for line in lines:
    nums_from_file.append(int(line.strip()))

total = sum(nums_from_file)
average = total / len(nums_from_file)

print("Part 2 numbers:", nums_from_file)
print("Part 2 average:", average)


with open("numbers.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")

print("Part 3 writing done")

with open("numbers.txt", "r") as file:
    lines = file.readlines()

nums_from_file2 = []
for line in lines:
    nums_from_file2.append(int(line.strip()))

total2 = sum(nums_from_file2)
average2 = total2 / len(nums_from_file2)

print("Part 3 numbers:", nums_from_file2)
print("Part 3 average:", average2)
