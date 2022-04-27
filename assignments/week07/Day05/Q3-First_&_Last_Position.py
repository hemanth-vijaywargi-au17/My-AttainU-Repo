"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""


def searchRange(arr, target):
    left = 0
    right = len(arr) - 1
    res = -1
    previous = 0

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            res = mid
            right = mid - 1  # In order to check if duplicates of target exist on the left side
        elif target > arr[mid]:
            left = mid + 1
            previous = mid
        else:
            right = mid - 1

    if res == -1:
        return [-1, -1]
    else:
        return [res, (res - 1 + arr.count(target))]


nums = [5, 7, 7, 8, 8, 10]
target = 8

print(searchRange(nums, target))

# Time Complexity: O(log n)
# Space Complexity: O(1)