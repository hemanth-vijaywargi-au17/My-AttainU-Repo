def climbStairs(pos, top):
    if pos == top:
        return 1
    if pos > top:
        return 0
    if dp[pos] != None:
        return dp[pos]
    ans = climbStairs(pos+1, top)+climbStairs(pos+2, top)
    dp[pos] = ans
    return ans


if __name__ == "__main__":
    dp = [None]*5
    print(climbStairs(0, 5))
