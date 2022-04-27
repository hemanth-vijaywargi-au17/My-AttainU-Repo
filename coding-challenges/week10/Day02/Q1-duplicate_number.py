def duplicate_num(nums):
    dict1 = dict()
    for i in nums:
        if i not in dict1:
            dict1[i] = None
        else:
            return i


arr = [1, 3, 4, 2, 2]
print(duplicate_num(arr))
