def Upper_Bound_Linear(arr, target):
    n = len(A)
    for i in range(-1, -n - 1, -1):
        if arr[i] == target:
            return n + i
    return -1


A = [1, 1, 1, 2, 2, 2, 3, 3, 4]
target = 2

print(Upper_Bound_Linear(A, target))


# Time Complexity is O(n)
# Space Complexity is O(1)

def Upper_Bound_Binary(arr, target):
    n = len(A)
    left = 0
    right = n - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return result


print(Upper_Bound_Binary(A, target))

# Time Complexity is O(log n)
# Space Complexity is O(1)

