"""
Q-2 )Next Greater Element I: (5 marks)
https://leetcode.com/problems/next-greater-element-i/
(Medium)
(See doubt session recording today to use stack to solve this problem)
You are given two integer arrays nums1 and nums2 both of unique elements,
where nums1 is a subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding
places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to
its right in nums2. If it does not exist, return -1 for this number.
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in
the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array
is 3.
For number 2 in the first array, there is no next greater number for it in the
second array, so output -1.
"""


# BruteForce Approach :
def nextGreater(nums1, nums2):
    list1 = []
    n2index = dict()
    for i in range(len(nums2)):
        n2index[nums2[i]] = i
    for i in range(len(nums1)):
        Found = False
        for j in range(n2index[nums1[i]] + 1, len(nums2)):
            if nums2[j] > nums1[i]:
                list1.append(nums2[j])
                Found = True
                break
        if not Found:
            list1.append(-1)
    return list1


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreater(nums1, nums2))


# Stack Approach :

def nextGreater1(nums1, nums2):
    n = len(nums1)

    result = [0] * n
    stack = []
    n1index = dict()

    for i in range(n):
        n1index[nums1[i]] = i

    for idx, val in enumerate(nums2):
        if len(stack) == 0:
            stack.append(idx)
        else:
            while len(stack) != 0 and val > nums2[stack[-1]]:
                if nums2[stack[-1]] in n1index:
                    result[n1index[nums2[stack[-1]]]] = val
                stack.pop()
            stack.append(idx)

    while len(stack) != 0:
        if nums2[stack[-1]] in n1index:
            result[n1index[nums2[stack[-1]]]] = -1
        stack.pop()

    return result


print(nextGreater1(nums1, nums2))
