def lengthOfLongestSubstring(s):
    char = set()
    left = 0
    right = 0
    max_L = 0

    while right < len(s):
        while s[right] in char:
            char.remove(s[left])
            left = left+1
        char.add(s[right])
        max_L = max(max_L, right-left+1)
        right += 1

    return max_L


if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
