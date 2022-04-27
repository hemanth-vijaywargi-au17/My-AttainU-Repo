def myPow(x, n, dp={}):
    if dp.get(n) != None:   # Checks if solution already exists in dictionary
        return dp[n]
    if n == 0 or x == 1:    # If number is 1 (or) power is 0 then answer is 1 
        return 1
    if n == 1:              # Anything power 1 is the number itself
        return x
    if x == 0:              # Zero Power anything is Zero
        return 0
    if n == -1:             # 2^-1 = 1/(2^1)
        return 1/x
    if n % 2 == 0:          # If power is even then , 2^10 = (2^5)^2
        ans = myPow(x, n//2, dp)**2
        dp[n] = ans
    else:                   # If power is odd then , 2^5 = (2^2) * (2^3)
        ans = myPow(x, n//2, dp) * myPow(x, (n//2+1), dp)
        dp[n] = ans
    return ans


if __name__ == "__main__":
    print(myPow(2, 1000))
