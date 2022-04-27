"""
Q-1 ) Squares of a Sorted Array:(5 marks) (easy)
https://leetcode.com/problems/squares-of-a-sorted-array/
Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""


# Simplest Approach : O(nlogn)
def sortedSquares1(nums):
    return sorted([i * i for i in nums])


# Using Two Pointers : O(n)
def sortedSquares(nums):
    n = len(nums)
    left = 0
    right = n - 1
    index = n - 1
    result = [0 for i in nums]

    while index >= 0:
        if abs(nums[left]) >= abs(nums[right]):
            result[index] = nums[left] ** 2
            left += 1
        else:
            result[index] = nums[right] ** 2
            right -= 1
        index -= 1

    for i in range(n):
        nums[i] = result[i]

    for i in range(n):
        nums[i] = result[i]
    return result


nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))
