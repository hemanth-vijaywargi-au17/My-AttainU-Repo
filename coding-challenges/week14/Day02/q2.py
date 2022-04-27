def subsetXORSum(nums):
    sumXor = 0
    for i in nums:
        sumXor |= i
    return sumXor * 2 ** (len(nums)-1)
