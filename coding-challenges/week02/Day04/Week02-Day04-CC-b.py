"""
b. Write a program that takes in 2 numbers and returns true if they are
divisible by each other. False otherwise.
[hint: use the bool() function]
"""

x = int(input("Enter the First Number : "))
y = int(input("Enter the Second Number : "))

Result = (not(bool(x%y))) or (not(bool(y%x)))

print("Are x and y divisible by each other ? :",Result)