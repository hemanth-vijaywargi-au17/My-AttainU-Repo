"""
https://leetcode.com/problems/search-a-2d-matrix/
"""

def binarySearch(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return False


""" Time Complexity : O(logm + logn) , 
    m = no. of rows , 
    n = no. of columns
"""
def searchMatrix(matrix, target):
    # Finding the Row in which our target might be present with Binary Search
    left = 0
    right = len(matrix)-1
    row = -1

    while left <= right:
        mid = (left+right)//2
        if matrix[mid][0] <= target:
            row = mid
            left = mid + 1
        else:
            right = mid-1

    if row == -1:
        return False
    # Again performing a Binary Search for target on the Row Found
    return binarySearch(matrix[row], target)


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 11
    print(searchMatrix(matrix, target))
