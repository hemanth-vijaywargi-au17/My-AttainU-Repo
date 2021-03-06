"""
Given an integer array , find all the numbers whose digit sum is even.
Input : - [1 , 2 , 1111,56 ,22 ,89 ,100]
Output: - [2 , 22 , 1111]
Example : 2 -> digit sum = 2
22 -> digit sum = 4
1111 -> digit sum = 4
"""


def Digit_Sum(n):
    string = str(n)
    sum = 0
    for i in string:
        sum = sum + int(i)
    return sum


def Even_Digit_Sum_List(list):
    list1 = []
    for i in list:
        if Digit_Sum(i) % 2 == 0:
            list1.append(i)
    return list1


number_list = [1, 2, 1111, 56, 22, 89, 100]
print(Even_Digit_Sum_List(number_list))

# Time Complexity is O(n*m)
# Space Complexity is O(n)