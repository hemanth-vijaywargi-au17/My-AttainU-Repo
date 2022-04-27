"""
Question : 3 -
------------------
Given an sorted integer array . Write a program to find UPPER Bound of
target number , return the index of the element .
Input : - [1,2,2,2,3,3,5,5,5,6,6,7,7] , target = 7
Output: - 12
"""

arr = [1, 2, 2, 2, 3, 3, 5, 5, 5, 6, 6, 7, 7]
target = 7


def Upper_Bound(arr, target):
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
        index = mid
        while True:
            if arr[index] == arr[mid]:
                index -= 1
            else:
                break
        return index + arr.count(arr[mid])
    else:
        return -1


print(Upper_Bound(arr, target))

# Time Complexity is O(log n)
# Space Complexity is O(1)
