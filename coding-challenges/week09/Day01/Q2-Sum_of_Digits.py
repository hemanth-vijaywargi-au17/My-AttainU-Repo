def digit_sum(n):
    if type(n) != str:
        n = str(n)
    if n == "":
        return 0
    return int(n[0]) + digit_sum(n[1:])


number = 12345

print(digit_sum(number))
