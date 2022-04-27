"""
Q-2 )Trapping Rain Water (7.5 marks)
https://leetcode.com/problems/trapping-rain-water/
(Hard)
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by
array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are
being trapped.
Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
(Hint: solve using stacks to precompute L and R list, of max element on right and
max element on left, respectively, for each element. Use formula
min(max_height_Right,max_height_Left)-current_height to get water level.
Use logic of just greatest element on the right question discussed on friday night
class)
"""


def water_trapped(height):
    n = len(height)
    max_until_now_left = -1
    max_until_now_right = -1
    max_left = [-1]
    max_right = [-1]
    for i in range(1, n):
        max_until_now_left = max(max_until_now_left, height[i - 1])
        max_until_now_right = max(max_until_now_right, height[n - i])
        max_left.append(max_until_now_left)
        max_right.append(max_until_now_right)
    max_right = max_right[::-1]

    total_water_trapped = 0
    for i in range(n):
        water_trapped_here = min(max_left[i], max_right[i]) - height[i]
        if water_trapped_here > 0:
            total_water_trapped += water_trapped_here

    return total_water_trapped


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height1 = [4, 2, 0, 3, 2, 5]
print(water_trapped(height))
print(water_trapped(height1))
