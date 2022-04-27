"""
Q-1 ) Pascal's Triangle (5 marks)
https://leetcode.com/problems/pascals-triangle/
(5 marks)
(Easy)
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
as shown:
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]
"""


def generate(numRows):

    res = [[1]]

    next_row = [1]
    for i in range(numRows-1):
        for i in range(len(res[-1])-1):
            next_row.append(res[-1][i]+res[-1][i+1])
        next_row.append(1)
        res.append(next_row)
        next_row = [1]

    return res


if __name__ == "__main__":
    rows = 10

    print(generate(rows))

    for row in generate(rows):
        print(" "*(rows-len(row)), *row)
