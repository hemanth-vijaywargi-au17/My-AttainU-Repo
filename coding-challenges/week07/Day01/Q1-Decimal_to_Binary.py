"""
Question 1 :
----------------
Given a decimal Number , Write a program to convert Decimal to Binary
number.
Input : 10 (decimal)
Output: - 1010
Explanation:
As, discussed in class , We can do %2 and //2 approach till the number is
positive and store the remainder and then reverse the same.
Sample :
def Decimal_to_Binary(number):
#write code here
"""

def Decimal_to_Binary(n):
    binary = ""
    while n > 0:
        r = n % 2
        n = n // 2
        binary += str(r)
        print("step",n)
    return binary[::-1]

print(Decimal_to_Binary(10))

# Time Complexity is O(log n)
# Space Complexity is O(1)
