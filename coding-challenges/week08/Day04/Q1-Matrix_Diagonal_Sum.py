def Matrix_Diag_Sum(arr,d):
    rows = len(arr)
    cols = len(arr[0])
    sum = 0
    if d=="right":
        for i in range(rows):
            for j in range(cols):
                if i + j == cols - 1:
                    sum += arr[i][j]
    elif d=="left":
        for i in range(rows):
            for j in range(cols):
                if i == j :
                    sum += arr[i][j]
    return f"{d.capitalize()} Diagonal Sum : {sum}"


Matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

Matrix2 = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]

Matrix3 = [[1, 2],
           [3, 4],
           [5, 6]]

print(Matrix_Diag_Sum(Matrix1,"right"))
