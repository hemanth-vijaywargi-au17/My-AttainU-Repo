"""
b. perform the same task as given above but using one for loop only instead of 2.
"""

n = int(input("Enter the number of lines : "))

halfway_point = ( n//2 + n%2 )

for ln in range(1, n+1):
    if (ln <= halfway_point):
        print(" "*(n-ln),"*"*(2*ln-1))
    else:
        print(" " * (ln-1), "*" * (2*(n+1-ln)-1))

