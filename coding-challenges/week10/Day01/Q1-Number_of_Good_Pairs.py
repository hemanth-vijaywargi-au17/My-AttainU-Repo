from collections import Counter
from math import factorial

"""
Q-1 ) Number of Good Pairs: (5 marks)
https://leetcode.com/problems/number-of-good-pairs/
Easy
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""


# BruteForce Approach : O(n^2)
def goodPairs(nums):
    n = len(nums)
    good_pairs = 0
    for i in range(n):
        for j in range(i, n):
            if i != j and nums[i] == nums[j]:
                good_pairs += 1
    return good_pairs


nums = [1, 2, 3, 1, 1, 3]
print(goodPairs(nums))

# Using Hash-Table :
"""
Algorithm :
1. Get counts of all numbers in the list and store in a dictionary.
2. Using permutations formula and counts we can find number of possible unique pairs.
        Permutations = n! / (n-r)! 
        n = number of items (count of a number in our case)
        r = number of items taken at a time (2 in our case ,since we need pairs)
Unique Permutations = permutations / 2
so , goodPairs = n! / 2*(n-2)! 
"""


def goodPairs1(nums):
    dict1 = dict(Counter(nums))
    good_pairs = 0
    for i in dict1.values():
        if i > 1:
            good_pairs += factorial(i) // (2 * factorial(i - 2))
    return good_pairs


print(goodPairs1(nums))
