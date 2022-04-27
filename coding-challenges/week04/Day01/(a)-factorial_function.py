"""
Define a function factorial() with one input n. [The default value of n needs to
be 5]. Use the factorial() function and other inbuilt functions to find the
maximum between the following:
1. 5!+3!-21 and 2!+4!+12
2. 26!+31! and 22!+35!
3. 21!+34!-15! and 31!+27!-19!
Hint: you can use the min() and max() inbuilt functions of python.
"""


def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact = num * fact
    return fact


a = factorial(5) + factorial(3) - 21
b = factorial(2) + factorial(4) + 12
print(f"(a) 5!+3!-21 = {a} \n(b) 2!+4!+12 = {b}")
print("Maximum :", max(a, b))
print()
c = factorial(26) + factorial(31)
d = factorial(22) + factorial(35)
print(f"(c) 26!+31! = {c} \n(d) 22!+35! = {d}")
print("Maximum :", max(c, d))
print()
e = factorial(21) + factorial(34) - 15
f = factorial(31) + factorial(27) - 19
print(f"(c) 21!+34!-15! = {e} \n(d) 31!+27!-19! = {f}")
print("Maximum :", max(e, f))
