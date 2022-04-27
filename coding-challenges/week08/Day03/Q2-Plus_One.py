# Q - 2 ) https://leetcode.com/problems/plus-one/
"""
Solve this question in any one approach other than the one discussed in
the class.

Code discussed in class:

class Solution:
    def plusOne(digits: list[int]) -> list[int]:
        sum = 0
        if digits[-1] == 9:
            wt = 1
            for i in digits[::-1]:
                sum += i*wt
                wt *= 10
            new = [int(i) for i in str(sum+1)]
            return new
        else:
            digits[-1] += 1
        return digits

Compare T(n) of your code and this code, don’t ignore constants in T(n)
"""

def plusOne(digits):
    for i in range(-1, -len(digits) - 1, -1):
        if digits[i] == 9:
            digits[i] = 0
            if i == -len(digits):
                digits.insert(0, 1)     # An insertion operation takes O(n) time complexity
        else:
            digits[i] += 1

    return digits

digits = [9, 9, 9, 9]

print(plusOne(digits))

# Time Complexity for both my code and class solution is O(2n) ,when not ignoring constants.
