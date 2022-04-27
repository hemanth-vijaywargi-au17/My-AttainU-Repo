from collections import Counter


# Sorting Approach
def anagram1(word1, word2):
    if len(word1) != len(word2):
        return False
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False


# Counter Approach (much faster than sorting as n increases)
def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    if Counter(word1) == Counter(word2):
        return True
    else:
        return False


word1 = "anagram"
word2 = "nagaram"

print(anagram(word1, word2))

print(anagram1(word1, word2))
