def Matrix_Border_Sum(arr):
    rows = len(arr)
    cols = len(arr[0])
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                sum += arr[i][j]
    return f"Matrix Border Sum : {sum}"


Matrix4 = [[1, 2, 3, 4],
           [4, 5, 6, 5],
           [7, 8, 9, 6],
           [4, 9, 8, 7]]

print(Matrix_Border_Sum(Matrix4))
