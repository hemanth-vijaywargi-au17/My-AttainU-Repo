"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than n / 2 times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


def majorityElement(nums):
    set1 = set(nums)
    majority_count = 0
    majority_element = 0
    for i in set1:
        count = nums.count(i)
        if count > majority_count:
            majority_element = i
            majority_count = count
    return majority_element


nums = [3, 2, 3]

print(majorityElement(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)