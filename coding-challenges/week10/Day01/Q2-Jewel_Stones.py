from collections import Counter

"""
Q-2 ) Jewels and StonesJewels and Stones: (5 marks)
https://leetcode.com/problems/jewels-and-stones/
You're given strings jewels representing the types of stones that are jewels, and
stones representing the stones you have. Each character in stones is a type of
stone you have. You want to know how many of the stones you have are also
jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
"""


def jewel_stones(jewels, stones):
    dict1 = dict(Counter(stones))
    jewel_stones = 0
    for i in jewels:
        if i in dict1:
            jewel_stones += dict1[i]
    return jewel_stones


jewels = "aA"
stones = "aAAbbbb"
print(jewel_stones(jewels, stones))
