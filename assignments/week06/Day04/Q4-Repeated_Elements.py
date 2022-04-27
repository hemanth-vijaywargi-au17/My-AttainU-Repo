"""
Given an array of size n and a number k, find all elements that appear
more than n/k times
Input : k = 4 ,n=9 , A = [ 3 ,1, 2, 2, 2, 1, 4, 3, 3 ]
Output: - [ 3 , 2]
Explanation : - val = n/k = (9/4) = 2 (integer part)
Now , take count of each element , we get
Count of element 3 -> 3
Count of element 1 -> 2
Count of element 2 -> 3
Count of element 4 -> 1
Since 3 and 2 are only elements which are having count greater than 2 .
"""

def Repeated_Elements(number_list,k):
    set1=set(number_list)
    list1=[]
    times=len(number_list)//k
    for i in set1:
        if number_list.count(i)>times:
            list1.append(i)
    return list1

A=[ 3 ,1, 2, 2, 2, 1, 4, 3, 3 ]
print(Repeated_Elements(A,4))

# Time Complexity is O(n)
# Space Complexity is O(n)

