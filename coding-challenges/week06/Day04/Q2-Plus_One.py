digits = [9,9,9,9]

for i in range(-1, -len(digits) - 1, -1):
    if digits[i] == 9:
        digits[i] = 0
        if i == -len(digits):
            digits.insert(0, 1)
    else:
        digits[i] += 1
        break

print(digits)
