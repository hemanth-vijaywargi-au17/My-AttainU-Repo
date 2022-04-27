"""
Lists are US - 1
Take 2 sequences of space separated integers as input from the user and convert
it into a list of integers. Extend the first list with all the items of the
second list and print the output.
Ex:
Input 1:
1 2 3 4
11 434 1
Output 1:
1 2 3 4 11 434 1
Input 2:
1 2 3
8 7
Output 2:
1 2 3 8 7
Hint: Consider using the inbuilt extend() function of lists in python
"""

# Taking input seperated by spaces and spliting at spaces ,any extra spaces
# will become list items as empty strings ("")
a = input("Enter numbers seperated by spaces :").split(" ")
b = input("Enter numbers seperated by spaces :").split(" ")

c=[]
d=[]

# It is possible that the user enters more than one space between numbers
# then below loops will filter and save non-empty strings in a new list
for i in range(0, len(a)):
    if a[i] != "":
        c.append(a[i])
for i in range(0, len(b)):
    if b[i] != "":
        d.append(b[i])

# Below loops will convert all items in our lists to integers
for i in range(0, len(c)):
    c[i] = int(c[i])
for i in range(0, len(d)):
    d[i] = int(d[i])

# Extending c with d using built-in function
c.extend(d)
print(c)
