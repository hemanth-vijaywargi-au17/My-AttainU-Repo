def LCS(str1, str2, idx1=0, idx2=0):
    if idx1 >= len(str1) or idx2 >= len(str2):
        return 0
    if dp[idx1][idx2] != None:
        return dp[idx1][idx2]
    if str1[idx1] == str2[idx2]:
        ans = 1 + LCS(str1, str2, idx1+1, idx2+1)
    else:
        dp[idx1+1][idx2] = LCS(str1, str2, idx1+1, idx2)
        dp[idx1][idx2+1] = LCS(str1, str2, idx1, idx2+1)
        ans = max(dp[idx1+1][idx2], dp[idx1][idx2+1])
    dp[idx1][idx2] = ans
    return ans


if __name__ == "__main__":
    str1 = "abcde"
    str2 = "ace"
    dp = [[None]*5]*5
    print(LCS(str1, str2))
