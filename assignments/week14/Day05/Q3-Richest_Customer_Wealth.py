"""
https://leetcode.com/problems/richest-customer-wealth/
"""


def maximumWealth(accounts):
    max_sum = 0
    for row in accounts:
        totalWealth = sum(row)
        if totalWealth > max_sum:
            max_sum = totalWealth
    return max_sum


if __name__ == "__main__":
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(maximumWealth(accounts))
