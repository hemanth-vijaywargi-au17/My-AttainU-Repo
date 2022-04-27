# This function can check if a number or any word is palindrome
def is_palindrome(string):
    if string == "":
        return True
    n = len(string)
    if string[0] != string[n - 1]:
        return False
    return is_palindrome(string[1:n - 1])


print(is_palindrome("12321"))  # Just pass the number as String
print(is_palindrome("mom"))
