"""
Assignment Week 3
[All questions need to be solved using both for and while loop]
1. Write code for the following sequence by taking line number as user input:

n = 5
**
 **
  **
 **
**

n=3
**
 **
**

2. Write code for the following sequence by taking line number as user input.

n = 3
  1
 121
12321

n = 4
   1
  121
 12321
1234321

3. Write code for the following sequence by taking line number as user input

n = 3
 1
121
 1

n = 5
  1
 121
12321
 121
  1

4. Write code for the following sequence by taking line number as user input, [using a single loop only]

n = 5
1
21
321
21
1

5. Write a function that takes line number as input (with default value of 5) and prints the following pattern.

n=3
.....
.. ..
.   .
.. ..
.....



n = 5
.......
... ...
..   ..
.     .
..   ..
... ...
.......

"""

# 1.

# Using for-loop

# n = int(input("Enter the number of lines : "))
n = 5

halfway_point = (n // 2 + n % 2)

for ln in range(1, n + 1):
    if ln <= halfway_point:
        print(" " * (ln - 1) + "*" * (2))
    else:
        print(" " * (n - ln) + "*" * (2))
print()
# Using while-loop

# n = int(input("Enter the number of lines : "))
n = 3

halfway_point = (n // 2 + n % 2)

ln = 1
while ln <= n:
    if (ln <= halfway_point):
        print(" " * (ln - 1) + "*" * (2))
        ln = ln + 1
    else:
        print(" " * (n - ln) + "*" * (2))
        ln = ln + 1
print()

# 2.

# Using for-loops

# n = int(input("Enter the number of lines : "))
n = 3

for ln in range(1, n + 1):

    print(" " * (n - ln), end="")

    for digit in range(1, ln + 1):
        print(digit, end="")

    for rev_digit in range(ln - 1, 0, -1):
        print(rev_digit, end="")

    print()
print()
# Using while-loops

# n = int(input("Enter the number of lines : "))
n = 4

ln = 1
while (ln <= n):

    print(" " * (n - ln), end="")

    digit = 1
    while digit <= ln:
        print(digit, end="")
        if ln == digit:

            rev_digit = ln - 1
            while rev_digit >= 1:
                print(rev_digit, end="")
                rev_digit = rev_digit - 1

        digit = digit + 1

    print()
    ln = ln + 1
print()

# 3.

# # Using for-loops

# n = int(input("Enter the number of lines (only odd numbers):  "))
n = 3

halfway_point = (n // 2 + n % 2)

for ln in range(1, halfway_point + 1):  # Loop for printing Triangle
    # Amount of spaces based on line number
    print(" " * (halfway_point - ln), end="")
    # Digits when increment
    for digit in range(1, ln + 1):
        print(digit, end="")
    # Digits when decrement
    for rev_digit in range(ln - 1, 0, -1):
        print(rev_digit, end="")
    # For new-line after finished printing a line
    print()

for ln in range(halfway_point - 1, 0, -1):  # Loop for Reverse-Triangle
    # Amount of spaces based on line number
    print(" " * (halfway_point - ln), end="")
    # Digits when increment
    for digit in range(1, ln + 1):
        print(digit, end="")
    # Digits when decrement
    for rev_digit in range(digit - 1, 0, -1):
        print(rev_digit, end="")
    # For new-line after finished printing a line
    print()
print()

# Using While-Loops

# n = int(input("Enter the number of lines (only odd numbers):  "))
n = 5
halfway_point = (n // 2 + n % 2)
ln = 1
while ln <= halfway_point:  # Loop for printing Triangle
    # Amount of spaces based on line number
    print(" " * (halfway_point - ln), end="")
    # Digits when increment
    digit = 1
    while digit <= ln:
        print(digit, end="")
        digit = digit + 1
    # Digits when decrement
    rev_digit = ln - 1
    while rev_digit >= 1:
        print(rev_digit, end="")
        rev_digit = rev_digit - 1
    # For new-line after finished printing a line
    print()
    ln = ln + 1
ln = halfway_point - 1
while ln >= 1:  # Loop for Reverse-Triangle
    # Amount of spaces based on line number
    print(" " * (halfway_point - ln), end="")
    # Digits when increment
    digit = 1
    while digit <= ln:
        print(digit, end="")
        digit = digit + 1
    # Digits when decrement
    rev_digit = ln - 1
    while rev_digit >= 1:
        print(rev_digit, end="")
        rev_digit = rev_digit - 1
    # For new-line after finished printing a line
    print()
    ln = ln - 1
print()

# 4.

# Using one For-Loop

n = 3
halfway_point = (n // 2 + n % 2)
string = ""
for ln in range(1, n + 1):
    if ln <= halfway_point:
        string = str(ln) + string
        print(string)
    else:
        print(string[ln - halfway_point:])
print()

# Using one While-Loop

n = 5
halfway_point = (n // 2 + n % 2)
string = ""
ln = 1
while ln <= n:
    if ln <= halfway_point:
        string = str(ln) + string
        print(string)
    else:
        print(string[ln - halfway_point:])
    ln = ln + 1
print()

# 5.

# Using for-loops

n = 3
halfway_point = n // 2 + n % 2
print("." * (n + 2))

for ln in range(1, halfway_point + 1):
    print("." * (((n + 1) // 2) + 1 - ln) + " " * (2 * ln - 1) + "." * (((n + 1) // 2) + 1 - ln), end="")
    print()

for ln in range(halfway_point - 1, 0, -1):
    print("." * (((n + 1) // 2) + 1 - ln) + " " * (2 * ln - 1) + "." * (((n + 1) // 2) + 1 - ln), end="")
    print()
print("." * (n + 2))
print()

# Using While-Loops

n = 5
halfway_point = n // 2 + n % 2
print("." * (n + 2))

ln = 1
while ln <= halfway_point:
    print("." * (((n + 1) // 2) + 1 - ln) + " " * (2 * ln - 1) + "." * (((n + 1) // 2) + 1 - ln), end="")
    print()
    ln = ln + 1

ln = halfway_point - 1
while ln >= 1:
    print("." * (((n + 1) // 2) + 1 - ln) + " " * (2 * ln - 1) + "." * (((n + 1) // 2) + 1 - ln), end="")
    print()
    ln = ln - 1
print("." * (n + 2))
