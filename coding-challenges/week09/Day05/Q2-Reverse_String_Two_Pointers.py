"""
Q-2 ) Reverse String:(5 marks) (easy)
Write a function that reverses a string. The input string is given as an array of characters
s.
https://leetcode.com/problems/reverse-string/
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""


# Normal Approach
def reverseString(s):
    n = len(s)
    for i in range(n // 2):
        s[i], s[n - 1 - i] = s[n - 1 - i], s[i]


# Using Two Pointers
def reverseString2(s):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s = ["h", "e", "l", "l", "o"]

reverseString2(s)
print(s)
