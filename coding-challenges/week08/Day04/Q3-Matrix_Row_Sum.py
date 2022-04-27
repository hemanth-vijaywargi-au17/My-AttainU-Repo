def Matrix_Row_Sums(arr):
    rows = len(arr)
    cols = len(arr[0])
    sums_list = []
    for i in range(rows):
        sum = 0
        for j in range(cols):
            sum += arr[i][j]
        sums_list.append(sum)
    return f"Matrix Row Sums : {sums_list}"


Matrix5 = [[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]]

print(Matrix_Row_Sums(Matrix5))
