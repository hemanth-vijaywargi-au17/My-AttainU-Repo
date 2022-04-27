"""
Q-1 ) Write a program to convert a string of binary number into a decimal
number: (5 marks)
(Easy)
eg:
Sample Input
st = “101”
Sample output
5
Revise the lecture to see the algorithm to convert binary to decimal
"""


def Binary_to_Decimal(bn):
    if type(bn) != str:
        bn = str(bn)
    x = 1
    decimal = 0
    for i in bn[::-1]:
        if i == "1":
            decimal += x
        x = x << 1
    return decimal


bn = "11111"
print(f"Binary number {bn} in Decimal form :", Binary_to_Decimal(bn))



"""
Q-2 ) Number of 1 Bits: (5 marks)
(Medium)
https://leetcode.com/problems/number-of-1-bits/
Write a function that takes an unsigned integer and returns the number of '1' bits
it has (also known as the Hamming weight).
Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has
a total of three '1' bits.

"""


def hammingWeight(n):
    if type(n) != str:
        n = str(n)
    return n.count("1")


print(f"Binary number {bn} has Hamming Weight :", hammingWeight(bn))



"""
Q-3 )Write a function to perform XOR between two positive integers: (5
marks), do not use the xor operator.
(Easy)
Sample Input:
A = 5
B = 3
Sample Output:
A^B = 6
explanation:
Take two inputs A and B as integers. => A = 5 , B = 3
Convert them to binary, => A = 101, B = 011
perform XOR operation, => A^B = 110
return resultant binary number as decimal number . => (110)base2 = (6)base10
"""


def Decimal_to_Binary(n):
    binary = ""
    while n > 0:
        r = n % 2
        n = n // 2
        binary += str(r)
    return binary[::-1]


def XOR(int1, int2):
    bn1 = Decimal_to_Binary(int1)
    bn2 = Decimal_to_Binary(int2)
    n1 = len(bn1)
    n2 = len(bn2)
    n = 0
    if n1 > n2:
        bn2 = "0" * (n1 - n2) + bn2
        n = n1
    else:
        bn1 = "0" * (n2 - n1) + bn1
        n = n2
    result = ""
    for i in range(n - 1, -1, -1):
        if bn1[i] == bn2[i]:
            result += "0"
        else:
            result += "1"
    result = result[::-1]
    return Binary_to_Decimal(result)


a = 2
b = 3
print(f"XOR Operation between {a} and {b} :", XOR(a, b))
print(f"XOR Operation between {a} and {a} :", XOR(a, a))
