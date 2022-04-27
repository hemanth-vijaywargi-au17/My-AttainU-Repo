from collections import Counter


def longestPalindrome(s):
    freq = Counter(s)
    ans = 0
    for letter in freq:
        if freq[letter] % 2 == 0:
            ans += freq[letter]
        else:
            ans += freq[letter]-1

    if ans < len(s):
        return ans+1
    return ans


if __name__ == "__main__":
    s = "abccccdd"
    print(longestPalindrome(s))
