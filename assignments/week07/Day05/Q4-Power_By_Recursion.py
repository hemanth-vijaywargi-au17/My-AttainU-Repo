"""
Q4.
Write a program to compute the power of a number.
Input - x = 10 , y = 5 , calculate = (x^y)
Output : - 100000
Example -
pow(n, 5) will give you n to the power 5. Use recursion in it.
def pow(x,y):
#write code here
"""


def pow(N, P):
    if P == 0:
        return 1
    if P == 1:
        return N
    else:
        return N * pow(N, P - 1)


print(pow(10, 5))

# Time Complexity: O(n)
# Space Complexity: O(1)
