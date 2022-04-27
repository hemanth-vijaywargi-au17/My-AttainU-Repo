"""
Q-3 ) Sort Colors
https://leetcode.com/problems/sort-colors/submissions/
"""

# Using Bubble-Sort
def sortColors(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if swapped == False:
            break


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)
