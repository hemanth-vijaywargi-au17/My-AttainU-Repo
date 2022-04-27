"""
Question 1 :
----------------
Given a sorted Integer array , Write a Program to search the target
element using Binary Search, If target element is found return the index .
Otherwise return -1 .
Input : arr = [1,2,3,15,16,19,23,55,1000] , target = 15
Output: - 3
Explanation:
Just Use Binary search method
Sample :
def Binarysearch(arr , target):
#write code here
"""

arr = [1, 2, 3, 15, 16, 19, 23, 55, 1000]
target = 15


def Binary_Search(arr, target):
    left = 0
    right = len(arr) - 1
    Found = False
    while left <= right and not Found:
        mid = (left + right) // 2
        if target == arr[mid]:
            Found = True
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if Found:
        return mid
    else:
        return -1


print(Binary_Search(arr, target))

# Time Complexity is O(log n)
# Space Complexity is O(1)
