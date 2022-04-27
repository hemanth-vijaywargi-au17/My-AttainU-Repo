def average(arr):
    n = len(arr)
    mini = arr[0]
    maxi = arr[0]
    total = arr[0]
    for i in range(1, n):
        total += arr[i]
        if arr[i] > maxi:
            maxi = arr[i]
        if arr[i] < mini:
            mini = arr[i]
    return (total - mini - maxi) / (n - 2)


salary = [4000, 3000, 1000, 2000]

print(average(salary))
