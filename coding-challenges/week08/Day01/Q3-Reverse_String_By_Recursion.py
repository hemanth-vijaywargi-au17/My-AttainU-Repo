"""
Q-3 ) Reverse a string using recursion:(5 marks)
If we have a string, write a function that prints reverse of that string, using
recursion.
Sample Input:
ABCD
Sample Output:
DCBA
"""

def Reverse_String(st):
    if st == '':
        return
    n = len(st)
    print(st[-1], end="")
    Reverse_String(st[:n - 1])

st = "ABCD"
Reverse_String(st)
