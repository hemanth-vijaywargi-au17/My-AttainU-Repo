def minMoves(nums):
    ans, min_element = 0, min(nums)

    for i in range(len(nums)):
        ans += nums[i] - min_element

    return ans


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(minMoves(nums))
