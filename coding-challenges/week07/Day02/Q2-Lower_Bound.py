"""
Questions:2
Given an sorted integer array . Write a program to find Lower Bound of
target number, return the index of the element
Input: arr = [1,2 ,3,3,3,4,4,5,5,7,7,7] , target = 6
Output: 8
Explanation : -
def Lower_Bound(arr , target):
#write code here
"""

# Binary Search

arr = [1, 2, 3, 3, 3, 4, 4, 5, 5, 7, 7, 7]
target = 6


def Lower_Bound(arr, target):
    left = 0
    right = len(arr) - 1
    Found = False
    while left <= right and not Found:
        mid = (left + right) // 2
        if arr[mid] < target:
            previous = mid
        if target == arr[mid]:
            Found = True
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if Found:
        index = mid
        while True:
            if arr[index] == arr[mid]:
                index -= 1
            else:
                break
        return index + 1
    else:
        return previous


print(Lower_Bound(arr, target))

# Time Complexity is O(log n)
# Space Complexity is O(1)
