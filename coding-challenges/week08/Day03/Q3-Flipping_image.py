# Q - 3) https://leetcode.com/problems/flipping-an-image/
"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the
resulting image.
To flip an image horizontally means that each row of the image is reversed.
● For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
● For example, inverting [0,1,1] results in [1,0,0].
Example 1:
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
"""


def flipAndInvertImage(image):
    for row in range(len(image)):
        image[row] = image[row][::-1]
        for column in range(len(image[row])):
            if image[row][column] == 1:
                image[row][column] = 0
            elif image[row][column] == 0:
                image[row][column] = 1
    return image


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(flipAndInvertImage(image))

# Time Complexity is O(n)
# Space Complexity is O(1)
