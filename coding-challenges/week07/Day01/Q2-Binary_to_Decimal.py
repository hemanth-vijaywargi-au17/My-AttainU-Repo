"""
Questions:2
Write a program to convert Binary number (given as list) to decimal
Integer
Input: [1,0,1]
Output: 5
Explanation : -
def Convert_Binary_to_Decimal(list1):
#write code here
"""

def Binary_to_Decimal(n):
    decimal = 0
    idx = -1
    for i in range(len(n)):
        if n[idx] == 1:
            decimal += 2 ** i
        idx -= 1
    return decimal

print(Binary_to_Decimal([1, 0, 1]))

# Time Complexity is O(n)
# Space Complexity is O(1)
