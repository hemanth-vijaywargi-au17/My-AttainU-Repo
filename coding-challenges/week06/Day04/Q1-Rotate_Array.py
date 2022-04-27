nums = [1, 2, 3, 4]
k = 2
for i in range(k):
    nums.insert(0, nums.pop(-1))
print(nums)
