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

"""
This Function returns the index of Lower Bound of target in the list.
If Target is not present :
    then it will return Upper Bound of Target's previous Element
"""

def Lower_Bound(arr, target):
    left = 0
    right = len(arr) - 1
    res = -1
    previous = 0
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            res = mid
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
            previous = mid
        else:
            right = mid - 1
    if res == -1:
        if target < arr[0]:
            return -1
        else:
            return previous
    else:
        return res


print(Lower_Bound(arr, target))

# Time Complexity is O(log n)
# Space Complexity is O(1)
