"""
Questions:2
Given a sorted array with Duplicates . Write a program to find UPPER
BOUND of a TARGET using Binary search Method .
Return Index corresponding to the element of the upper bound element.
Example :
Input : - arr = [1,1,1,2,2,3,3,5,5,5,7,7] , Target = 4
Output : - 7
def Upper_Bound(arr , target):
#write code here
"""

arr = [1, 1, 1, 2, 2, 3, 3, 5, 5, 5, 7, 7]
target = 4

"""
This Function returns the index of Upper Bound of target in the list.
If Target is not present :
    then it will return Lower Bound of Target's next Element
"""


def Upper_Bound(arr, target):
    left = 0
    right = len(arr) - 1
    res = -1
    next = 0

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            res = mid
            left = mid + 1      # In order to check if duplicates of target exist on the right side
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
            next = mid

    if res == -1:
        if target > arr[-1]:
            return -1
        else:
            return next
    else:
        return res


print(Upper_Bound(arr, target))

# Time Complexity is O(log n)
# Space Complexity is O(1)
