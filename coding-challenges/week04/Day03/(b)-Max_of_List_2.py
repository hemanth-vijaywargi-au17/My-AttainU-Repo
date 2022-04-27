"""
Max of a list - 2
Write a function called MaxSeq() which can take any number of inputs from the
user and returns the highest number in that sequence as the output.
[You cannot use the inbuilt function max() of python]
Ex:
Input 1:
11 2 3 4
Output 1:
11
Input 2:
1 2 3 8 7
Output 2:
8
Hint: https://www.programiz.com/python-programming/args-and-kwargs visit this
link to understand how to call a python function with multiple inputs.
"""

# A function which can take any number of inputs and returns the highest number
def MaxSeq(*numbers):
    largest = 0
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if numbers[i] > largest:
                largest = numbers[i]
    return largest

print(MaxSeq(11,2,3,4))
print(MaxSeq(1,2,3,8,7))
