def maxPathSum(m, dp, r=0, c=0):
    if r == len(m) or c == len(m[r]) or c < 0:
        return 0

    if r == len(m)-1:
        return m[r][c]

    if dp[r][c] != None:
        return dp[r][c]

    move1 = m[r][c] + maxPathSum(m, dp, r+1, c)    # Go Down Straight
    move2 = m[r][c] + maxPathSum(m, dp, r+1, c-1)  # Go Down Left
    move3 = m[r][c] + maxPathSum(m, dp, r+1, c+1)  # Go Down Right

    ans = max(move1, move2, move3)
    dp[r][c] = ans

    next_col_ans = maxPathSum(m, dp, r, c+1)
    dp[r][c+1] = next_col_ans

    return max(ans, next_col_ans)


def maximumPath(matrix):
    row = len(matrix)
    col = len(matrix[0])
    dp = [[None for i in range(col+1)] for i in range(row-1)]
    return maxPathSum(matrix, dp)


if __name__ == "__main__":
    matrix = [[348, 391], [618, 193]]
    print(maximumPath(matrix))
