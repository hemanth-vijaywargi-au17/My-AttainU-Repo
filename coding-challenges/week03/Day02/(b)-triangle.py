"""
b. Given a number as input from the user, print a triangle like the following.
if input is 3:
*
**
***
**
*
if input is 5:
*
**
***
****
*****
****
***
**
*
give codes containing for loop and while loop
"""

# using for loops
n=int(input("Enter the size : "))
for i in range(1,n+1):
    print("*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i)

# using While loops
n=int(input("Enter the size : "))
i=1
while(i<=n):
    print("*" * i)
    i=i+1

i=n-1
while(i>=1):
    print("*" * i)
    i = i - 1













