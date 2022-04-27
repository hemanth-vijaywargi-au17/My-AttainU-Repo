"""
Given a integer array , find all the numbers which are palindrome:
Note : -Palindromes are numbers when reversed will get the same as the
original number.
121 - >palindrome , 123 → not a palindrome
Input: [1 , 2 , 256 , 252 , 1441 , 969 ,2331]
Output: [1 , 2 , 252 , 1441 , 969 ]
"""


def is_palindrome(n):
    string = str(n)
    if string == string[::-1]:
        return True
    else:
        return False

def palindrome_list(list):
    palindromes = []
    for i in list:
        if is_palindrome(i):
            palindromes.append(i)
    return palindromes

number_list = [1, 2, 256, 252, 1441, 969, 2331]

print(palindrome_list(number_list))

# Time Complexity is O(n)
# Space Complexity is O(n)