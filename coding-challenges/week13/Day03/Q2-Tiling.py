def tiling(n,m):
    if n==m:
        return 1
    if n<m:
        return 1+tiling(n,m-n)
    else:
        return 1+tiling(n-m,m)

print(tiling(2,3))