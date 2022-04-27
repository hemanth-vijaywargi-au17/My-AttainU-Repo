"""
Q-1 ) Valid Parentheses:
https://leetcode.com/problems/valid-parentheses/
(5 marks)
(Easy)
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Example 1:
Input: s = "()"
Output: true
"""


def Valid_Parenthesis(s):
    pairs = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for c in s:
        if c in pairs:
            stack.append(c)
        elif len(stack) > 0 and pairs[stack[-1]] == c:
            stack.pop()
        else:
            return False
    return len(stack) == 0


s = "]["
print(Valid_Parenthesis(s))
