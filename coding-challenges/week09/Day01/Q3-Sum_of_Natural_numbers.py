# Simple Approach
def natural_sum(n):
    return n * (n + 1) // 2


print(natural_sum(10))


# Recursive Approach
def natural_sum_rec(n):
    if n == 1:
        return 1
    return n + natural_sum_rec(n - 1)


print(natural_sum_rec(10))
