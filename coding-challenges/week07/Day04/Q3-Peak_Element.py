"""
Questions:3
Given an array with NO Duplicates . Write a program to find PEAK
ELEMENT
Return value corresponding to the element of the peak element.
Example :
Input : - arr = [2,5,3,7,9,13,8]
Output : - 5 or 13 (anyone)
HINT : - Peak element is the element which is greater than both
neighbours.
def FindPeak(arr ):
#write code here
"""

arr = [2, 5, 3, 7, 9, 13, 8]


def Find_Peak(arr):
    n = len(arr)
    for i in range(n):
        if i == 0 and arr[i] > arr[i + 1]:
            return arr[i]
        elif i == n - 1 and arr[i] > arr[i - 1]:
            return arr[i]
        elif arr[i - 1] < arr[i] > arr[i + 1]:
            return arr[i]


print(Find_Peak(arr))

# Time Complexity is O(n)
# Space Complexity is O(1)
