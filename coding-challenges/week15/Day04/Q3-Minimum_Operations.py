def minOperations(nums, x):
    n = len(nums)
    target = sum(nums) - x
    # We need to find the Length of Longest Subarray with Sum = Target
    left = 0
    max_length = -1
    running_sum = 0
    for right in range(n):
        running_sum += nums[right]

        while running_sum > target and left <= right:
            running_sum -= nums[left]
            left += 1

        if running_sum == target:
            max_length = max(max_length, right-left+1)

    return n - max_length if max_length != -1 else -1


if __name__ == "__main__":
    nums = [3, 2, 20, 1, 1, 3]
    x = 10
    print(minOperations(nums, x))
