"""
Given a non-negative integer x, compute and return the square root of x.
Note: You are not allowed to use any built-in exponent function or operator,
      such as pow(x, 0.5) or x ** 0.5.
"""

def Sqrt(x):
    if (x == 0 or x == 1):
        return x
    i = 1
    result = 1
    while (result <= x):
        i += 1
        result = i * i
    return i - 1

x = 8
print(Sqrt(x))

# Time Complexity: O(√n)
# Space Complexity: O(1)
