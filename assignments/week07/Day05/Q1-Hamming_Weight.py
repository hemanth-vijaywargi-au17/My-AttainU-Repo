"""
Question 1 :
--------------
Given a number N , count number of SET bits (having 1) in binary format of number N.
Also known as Hamming Weight.
INPUT - 26
OUTPUT : 3
Explanation :
N = 26 , binary value = 11010 , count of set bits (having value 1) = 3.
HINT : - Make use of bit manipulation concept .
"""


def Decimal_to_Binary(n):
    binary = ""
    while n > 0:
        r = n % 2
        n = n // 2
        binary += str(r)
    return binary[::-1]


def hammingWeight(n):
    n = Decimal_to_Binary(n)
    return n.count("1")


print(hammingWeight(26))

# Time Complexity: O(n)
# Space Complexity: O(1)
