"""
https://leetcode.com/problems/flipping-an-image/
"""


def flipAndInvertImage(image):
    for row in image:
        n = len(row)
        for i in range((n+1)//2):
            row[i], row[n-1-i] = row[n-1-i] ^ 1, row[i] ^ 1
    return image


if __name__ == "__main__":
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(flipAndInvertImage(image))
