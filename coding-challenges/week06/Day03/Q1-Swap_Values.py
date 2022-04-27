"""
Question 1 :
---------------
Write a Program to swap values , without using 3rd variable .
Also find Time and Space Complexity --- Marks : - 5
Example : -
Input : -
A = 20 , B = 10
Output : - A = 10 , B = 20
Explanation : - values has been swapped
Sample :
Def swap(A,B):
#write code here
"""

a, b = int(input("a = ")), int(input("b = "))

a, b = b, a

print(f"Swapped \na = {a} , b = {b}")

# Time Complexity is O(1)
# Space Complexity is O(1)

