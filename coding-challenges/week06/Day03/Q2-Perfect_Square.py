"""
Question : 2 -
Given a number , find if the number is a perfect square root or not ? --- Marks :-5
Also , find Time and space Complexity
example :
Input : n = 4
output : - True
Input : n = 10
output : - False
Explanation : since square root (4) =2 (perfect square ) --true
Square root(10) = 3.35 (Not perfect square) -- false
Sample :
Def find_perfect_square(N):
# write code here
"""

def find_perfect_square(n):
    if n ** (1 / 2) == int(n ** (1 / 2)):
        return True
    else:
        return False

print(find_perfect_square(int(input("n = "))))

# Space Complexity is O(1)
# Time Complexity is O(1)