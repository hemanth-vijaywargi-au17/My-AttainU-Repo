"""
Q-3 )Maximum Ascending Subarray Sum: (5 marks) (easy)
https://leetcode.com/problems/maximum-ascending-subarray-sum/
Given an array of positive integers nums, return the maximum possible sum of an
ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r,
numsi < numsi+1. Note that a subarray of size 1 is ascending.
Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
"""


def maxAscendingSum(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    max_sum = 0
    curr_sum = 0

    for i in range(n - 1):
        curr_sum += nums[i]
        if nums[i] >= nums[i + 1]:
            max_sum = max(max_sum, curr_sum)
            curr_sum = 0
    if curr_sum != 0:
        curr_sum += nums[n - 1]
    return max(curr_sum, max_sum)


nums = [10, 20, 30, 5, 10, 50]

print(maxAscendingSum(nums))
