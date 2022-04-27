# Q-1 ) MCQ
# Answer : (a)



"""
Q-2 ) What is the worst case complexity of selection sort? (5 marks)
a) O(n logn)
b) O(logn)
c) O(n)
d) O(n^2)

# Answer : d) O(n^2)
"""




"""
Q-3),Q-4) Selection Sort
1. First Select element
2. Compare it with all elements in the list (excluding it-self and elements at the previous position)
3. if an element is found to be smaller than our first selection then swap them
4. In the end you will have smallest element at position 1
5. Select next number do the above four steps again
6 .Everytime Searching area is reduced
"""

# With for-loop
def selection_sort(list):
    n = len(list)
    arr = list[:]
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


# With While-loop
def selection_sort1(list):
    n = len(list)
    arr = list[:]
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
            j += 1
        i += 1
    return arr


arr = [5, 2, 4, 1, 3]
arr1 = [23, 67, 8, 0, -3]

print(selection_sort(arr))
print(selection_sort1(arr1))

# Time Complexity is O(n^2)
# Space Complexity is O(n)
