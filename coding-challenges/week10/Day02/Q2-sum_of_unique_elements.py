def unique_sum(nums):
    dict1 = dict()
    total = 0
    for i in nums:
        if i not in dict1:
            dict1[i] = 1
            total += i
        else:
            dict1[i] += 1
            if dict1[i] == 2:
                total -= i
    return total


arr = [1, 3, 4, 2, 2, 5, 2]
print(unique_sum(arr))
