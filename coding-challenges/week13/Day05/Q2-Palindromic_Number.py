# Palindromic Number : Time O(logn) , Space O(1)
def isPalindrome(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    rev = 0
    while rev < x:
        a = x % 10
        rev = rev*10+a
        x = x//10

    return rev == x or rev//10 == x


if __name__ == "__main__":
    n = 121
    print(isPalindrome(n))
