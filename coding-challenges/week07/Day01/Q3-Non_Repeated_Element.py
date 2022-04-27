"""
Question : 3 -
------------------
Given an integer array , every element is repeated TWICE , except one
element , Find that element ?
Input : - [1 , 2 , 1 , 2 , 4 , 5 , 3 , 4 , 3]
Output: - 5
Explanation : HINT : - Use XOR operator ;
"""

def Non_Repeated_Element(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res = res ^ arr[i]
    return res

arr = [1, 2, 1, 2, 4, 5, 3, 4, 3]

print("Element which appeared only Once :", Non_Repeated_Element(arr))

# Time Complexity is O(n)
# Space Complexity is O(1)
