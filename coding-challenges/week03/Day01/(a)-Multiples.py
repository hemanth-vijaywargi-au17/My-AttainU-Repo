"""
a. Take a number as input from the user, print its multiple of 2, 4, 6,
8, 10 if it is an odd number, if it is an even number then print its
multiple of 1, 3, 5, 7 and 9.

"""

x = int(input("Enter a Number : "))

if (x%2!=0):
    print(x*2, "," ,x*4, "," ,x*6, "," ,x*8, "," ,x*10)
else:
    print(x*1, "," ,x*3, "," ,x*5, "," ,x*7, "," ,x*9)