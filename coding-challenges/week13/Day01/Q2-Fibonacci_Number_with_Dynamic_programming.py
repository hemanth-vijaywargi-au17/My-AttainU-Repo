def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n] != None:
        return dp[n]
    ans = fibonacci(n-1)+fibonacci(n-2)
    dp[n] = ans
    return ans


if __name__ == "__main__":
    dp = [None]*101
    for i in range(101):
        print(fibonacci(i))
