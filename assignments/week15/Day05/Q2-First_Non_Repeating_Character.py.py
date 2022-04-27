"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""
from collections import Counter


def firstUniqChar(s):
    freq = Counter(s)
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    return -1


if __name__ == "__main__":
    s = "leetcode"
    print(firstUniqChar(s))
