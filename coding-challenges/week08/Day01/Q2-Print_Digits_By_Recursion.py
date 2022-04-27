"""
Q-2 ) Write a function that prints digits of a number from left to right , using
recursion:(5 marks)
Sample Input:
1234567
Sample output:
1
2
3
4
5
6
7
"""

def Print_Digits(n):
    if n == '':
        return
    if type(n) is int:
        n = str(n)
    print(n[0])
    Print_Digits(n[1:])

n = 1234567
Print_Digits(n)
