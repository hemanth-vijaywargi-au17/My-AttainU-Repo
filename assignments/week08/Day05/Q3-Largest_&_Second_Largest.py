def Largest(arr):
    n = len(arr)
    Largest = 0
    Second_Largest = 0

    for i in range(n):
        if arr[i] > Largest:
            Largest = arr[i]

    for i in range(n):
        if arr[i] > Second_Largest and arr[i] < Largest:
            Second_Largest = arr[i]

    return f"Largest : {Largest}\nSecond Largest : {Second_Largest}"


A = [1, 3, 4, 5, 8, 1, 2, 3, 4, 9, 6, 9]

print(Largest(A))

# Time Complexity is O(n)
# Space Complexity is O(1)
