"""
Q-2 ) Pascal's Triangle II (5 marks)
https://leetcode.com/problems/pascals-triangle-ii/
(Easy)
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's
triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
as shown:
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:
Input: rowIndex = 0
Output: [1]
"""


def getRow(rowIndex):
    numRows = rowIndex+1
    res = [[1]]

    next_row = [1]
    for i in range(numRows-1):
        for i in range(len(res[-1])-1):
            next_row.append(res[-1][i]+res[-1][i+1])
        next_row.append(1)
        res.append(next_row)
        next_row = [1]

    return res[-1]


if __name__ == "__main__":
    print(getRow(4))    # 5th Row in Pascal's Triangle
