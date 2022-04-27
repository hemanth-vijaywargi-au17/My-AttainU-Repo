def uniquePathsIII(grid):
    m, n = len(grid), len(grid[0])
    total = 0

    def dfs(grid, x, y, vis, total):
        nonlocal paths
        if not (0 <= x < m and 0 <= y < n):
            return
        if grid[x][y] == 2:
            if total+1 == vis:
                paths += 1
            return
        if grid[x][y] == -1:
            return
        if grid[x][y] == float('inf'):
            return
        val = grid[x][y]
        grid[x][y] = float('inf')
        dfs(grid, x+1, y, vis+1, total)
        dfs(grid, x-1, y, vis+1, total)
        dfs(grid, x, y-1, vis+1, total)
        dfs(grid, x, y+1, vis+1, total)
        grid[x][y] = val

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                total += 1
            if grid[i][j] == 1:
                x, y = i, j
    paths = 0
    dfs(grid, x, y, 0, total)
    return paths


if __name__ == "__main__":
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    print(uniquePathsIII(grid))
