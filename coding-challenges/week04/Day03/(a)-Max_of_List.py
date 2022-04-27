"""
Max of a list
Write a function which takes a list as an input from the user [using the input()
command] and returns the highest and the second highest elements of a list.
Ex:
Input 1:
1 2 3 4
Output 1:
3 4
Input 2:
1 2 3 8 7
Output 2:
7 8
"""


def max_of_list():
    a = input("Enter numbers separated by spaces : ").split(" ")

    b = []

    # It is possible that the user enters more than one space between numbers
    # then below loop will filter and save non-empty strings in a new list
    for i in range(0, len(a)):
        if a[i] != "":
            b.append(a[i])

    # Below loop will convert all items in our list to integers
    for i in range(0, len(b)):
        b[i] = int(b[i])

    x = max(b)
    b.remove(max(b))
    y = max(b)

    print(f"Second highest : {y} , Highest : {x}")


max_of_list()
