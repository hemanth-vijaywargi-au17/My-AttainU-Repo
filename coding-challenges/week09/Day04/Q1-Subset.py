# Q-1 ) Find whether an array is subset of another array:

def is_subset(arr1, arr2):
    B = set(arr2)
    if set(arr1) & B == B:  # & operator returns intersection of sets
        return True
    else:
        return False


arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [1, 2, 4]
arr3 = {11, 1, 13, 21, 3, 7}
arr4 = {11, 3, 7, 1}

print(is_subset(arr1, arr2))
print(is_subset(arr3, arr4))
