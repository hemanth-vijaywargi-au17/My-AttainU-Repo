def climbStairs(pos, top):
    if pos == top:
        return 1
    if pos > top:
        return 0
    ans = climbStairs(pos+1, top)+climbStairs(pos+2, top)
    return ans

if __name__=="__main__":
    print(climbStairs(0, 5))
