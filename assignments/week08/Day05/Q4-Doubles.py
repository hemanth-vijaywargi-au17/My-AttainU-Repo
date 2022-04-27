def Doubles(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if i != j and (arr[i] == 2 * arr[j] or arr[i] == arr[j] / 2):
                return True
    return False


arr = [-2, 0, 10, -19, 4, 6, -8]

print(Doubles(arr))

# Time Complexity is O(n^2)
# Space Complexity is O(1)

