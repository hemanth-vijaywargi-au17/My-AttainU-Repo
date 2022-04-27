"""
Q-1 ) Recursive implementation of atoi() function:(5 marks)
Atoi() function converts a string into an integer.
eg:
st = “1234” is a string.
if we perform,
st + 1
this results in error since “st” is a string and 1 is an integer, and,
st + “1”
this will append 1 into 1234. Giving us 12341.
write a function that converts the above variable ‘st’ into an integer (so that we
can perform mathematical operations on it).
Sample input:
“1234”
Sample output:
1234
"""

# Works for Both Positive and Negative Numbered Strings

def myAtoiRecursive(st):
    if st == '':
        return 0
    negative = False
    if st[0] == "-":
        st = st[1:]
        negative = True
    n = len(st)
    multiplier = 10 ** (n - 1)
    number = int(st[0]) * multiplier + myAtoiRecursive(st[1:])
    if negative:
        return -number
    else:
        return number


print(myAtoiRecursive("-1234"))



# For Positive Numbered Strings Only :
#
# def myAtoiRecursive(st):
#     if st == '':
#         return 0
#     n = len(st)
#     multiplier = 10 ** (n - 1)
#     return int(st[0]) * multiplier + myAtoiRecursive(st[1:])
#
# print(myAtoiRecursive("1234"))
