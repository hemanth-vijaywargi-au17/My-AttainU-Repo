def Multiply(x, y):
    if y == 1:
        return x
    return x + Multiply(x, y - 1)


print(Multiply(5, 3))
