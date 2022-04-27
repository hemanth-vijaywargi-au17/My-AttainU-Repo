"""
Question 1 :
----------------
Given a sorted array with Duplicates . Write a program to find LOWER
BOUND of a TARGET using Binary search Method .
Return Index corresponding the element of lower bound element.
Example :
Input : - arr = [1,1,1,2,2,3,3,5,5,5,7,7] , Target = 4
Output : - 6
def Lower_Bound(arr , target):
#write code here
"""

arr = [1, 1, 1, 2, 2, 3, 3, 5, 5, 5, 7, 7]

target = 4

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
            right = mid - 1     # In order to check if duplicates of target exist on the left side
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
