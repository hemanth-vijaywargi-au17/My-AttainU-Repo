"""
Given an array arr[], find the maximum j – i such that arr[j] > arr[i] .
Input :- arr = [ 34, 8, 10, 3, 2, 80, 30, 33, 1]
Output : - 6 (j = 7, i = 1)
Explanation : -
Since at index ( j = 6 and i = 1 ) , we get maximum ( j - i ) where arr[j] > arr[i]
Sample :
Def find_max ( arr ):
"""

def find_max(arr):
    max = 0
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            if arr[j] > arr[i] and j - i > max:
                max = j - i
    return max

arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]

print(find_max(arr))

# Time Complexity is O(n^2)
# Space Complexity is O(1)