"""
a. Given a number as input from the user, print all its odd multiples from 1 to 21 if the number is odd
and all even multiples from 2 to 20 if the number is even.
Use both for loop and while loop.
"""

# Using for loop
x = int(input("Enter a Number : "))
if(x%2 != 0):
    for i in range(1,22,2):
        print(i * x)
else:
    for i in range(2,21,2):
        print(i * x)

# Using while loop
x = int(input("Enter a Number : "))
if(x%2 != 0):
    i=1
    while(i <= 21):
        print(i * x)
        i = i + 2
else:
    i = 2
    while (i <= 20):
        print(i * x)
        i = i + 2