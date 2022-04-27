# Two Pointer Approach : Time Complexity : O(n+m) , Space Complexity : O(1)
def isSubsequence(t, s):
    n = len(t)
    m = len(s)
    p1 = 0   
    p2 = 0
    while p1 < n and p2 < m:
        if t[p1] == s[p2]:
            p1 += 1
            p2 += 1
        else:
            p1 += 1

    if p1 == n and p2 != m: # If t has ended before s , then automatically s is not a subseq of t
        return False

    return True


if __name__ == "__main__":
    t = "abcde"
    s = "ace"
    print(isSubsequence(t, s))
