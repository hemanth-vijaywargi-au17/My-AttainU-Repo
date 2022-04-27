"""
Q-3 ) Sort an array in wave form :
Given an unsorted array of integers, sort the array into a wave like array. An
array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <=
arr[4] >= …..
Examples:
Input: arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80}
                            OR
                {20, 5, 10, 2, 80, 6, 100, 3}
                            OR
                any other array that is in wave form
"""


def wave_form_sort(list):
    arr = list[:]
    n = len(arr)
    for i in range(n - 1):
        if i % 2 == 0 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        elif i % 2 == 1 and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Test_Cases
arr  = [10, 5, 6, 3, 2, 20, 100, 80]    # Unsorted List
arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Sorted List (Descending)
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Sorted List (Ascending)

print(wave_form_sort(arr))
print(wave_form_sort(arr1))
print(wave_form_sort(arr2))
