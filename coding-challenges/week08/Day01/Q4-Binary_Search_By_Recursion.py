"""
Q-4 ) [Bonus Question] Recursive implementation of binary search:
(5 extra marks)
We have seen an iterative approach for binary search algorithm , write a
recursive approach for that.
HINT: when we divide the array into two parts, we need to perform a search on only one half.
Apply binary search only on that half.
"""

def Binary_Search(arr, target, left, right):
    mid = (left + right) // 2

    if target == arr[mid]:
        return mid
    elif mid == len(arr) - 1 or mid == 0:
        return -1
    elif target > arr[mid]:
        left = mid + 1
    elif target < arr[mid]:
        right = mid - 1
    return Binary_Search(arr, target, left, right)


arr = [1, 2, 3, 15, 16, 19, 23, 55, 1000]
target = 15
n = len(arr)

print(Binary_Search(arr, target, 0, n - 1))
