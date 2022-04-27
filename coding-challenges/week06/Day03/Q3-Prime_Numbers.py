"""
Questions : 3 --
Print prime numbers between 1 to N : ---marks: 5
using for loop :
Also , find the Time and Space complexity
Example : -
Input : - N = 10
output : - [2 , 3 , 5 , 7 ]
Explanation : - 2 , 3 , 5 , 7 are primes number between 1 to 10
Sample :-
Def Prime_number(N):
#write code here
"""

def factors(n):
    div = 1
    list1 = []
    while div <= n:
        if n % div == 0:
            list1.append(div)
        div = div + 1
    return list1

def Prime_number(n):
    list1 = []
    for i in range(2, n + 1):
        if len(factors(i)) < 3:
            list1.append(i)
    return list1

print(Prime_number(5))

# Time Complexity is O(n^2) , so it is an extremely slow algorithm as n increases.
# Space Complexity is O(n)