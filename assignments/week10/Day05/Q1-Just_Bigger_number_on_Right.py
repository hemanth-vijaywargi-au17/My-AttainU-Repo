"""
Q-1 ) Given a list, Write a brute force approach without using stacks(using
for loops, so that you can appreciate the beauty of stacks) to find the just
larger element on the right of the element, for each element.
And for last element, since there is no element on the right give “None”:
(5 marks)
(Easy)
Example 1:
Input: [2,1,7,4,6,8,1,9]
Output: [7,7,8,6,8,9,9,None]
"""

# BruteForce Approach : O(n^2)
def justBigger1(nums):
    n = len(nums)
    nums1 = []
    for i in range(n):
        Found = False
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                nums1.append(nums[j])
                Found = True
                break
        if not Found:
            nums1.append(None)
    return nums1


nums = [1, 50, 3, 7, 8, 9, 9, 9]
print(justBigger1(nums))


# Stack Approach : O(n)
def justBigger(nums):
    stack = []
    result = [0] * len(nums)
    for idx, val in enumerate(nums):
        if len(stack) == 0:
            stack.append(idx)
        else:
            while len(stack) != 0 and val > nums[stack[-1]]:
                result[stack[-1]] = val
                stack.pop()
            stack.append(idx)
    while len(stack) != 0:
        result[stack[-1]] = None
        stack.pop()
    return result


nums = [1, 50, 3, 7, 8, 9, 9, 9]
print(justBigger(nums))
