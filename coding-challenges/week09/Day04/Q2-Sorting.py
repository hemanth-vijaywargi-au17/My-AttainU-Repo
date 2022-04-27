"""
Q-2 )Sort an array of 0s, 1s and 2s:(5 marks)
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that
sorts the given array. The functions should put all 0s first, then all 1s and all 2s in
last.
Examples:
Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}
Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
"""

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

n = len(arr)
c_0 = 0
c_1 = 0

# Counting number of 0s and 1s in the array
for i in arr:
    if i == 0:
        c_0 += 1
    elif i == 1:
        c_1 += 1

# Modifying arr in-place
for i in range(n):
    if i < c_0:
        arr[i] = 0
    elif i >= c_0 and i < c_0 + c_1:
        arr[i] = 1
    else:
        arr[i] = 2

print(arr)

# Above is a Two-Pass Algorithm

