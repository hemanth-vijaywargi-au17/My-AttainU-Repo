"""
Q - 4 ) (Objective of this question is to make you utilise memory(space better))
Reverse an array of integers and do not use inbuilt functions like “reverse”,
don’t use shorts hands like “arr[::-1]”. Only use following approach:
swap first and last element,
then second and second last element,
till middle.
DO NOT USE TEMPORARY VARIABLE TO SWAP TWO VARIABLES.
"""

def reverse_array(arr):
    n = len(arr)
    m = -1
    for i in range(n//2):   # Swapping involves two numbers at a time , so we need n/2 steps
        arr[i], arr[m] = arr[m], arr[i]
        m -= 1
    return arr

arr = [1, 2, 3, 4, 5]

print(reverse_array(arr))

# Time Complexity is O(n)
# Space Complexity is O(1)
