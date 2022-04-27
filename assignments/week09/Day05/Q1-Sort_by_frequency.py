from collections import Counter

"""
Problem : Sort a list of numbers based on their frequency 
          and if frequency is same for two or more numbers,
          then sort them in decreasing order
"""


def freq_sort(arr):
    dict1 = dict(Counter(arr))
    dict2 = dict()

    for value in dict1.values():
        dict2[value] = []

    for number_key in dict1.keys():
        for freq_key in dict2.keys():
            if dict1[number_key] == freq_key:
                dict2[freq_key].append(number_key)

    groups = dict(sorted(dict2.items()))

    for key in groups.keys():
        groups[key] = sorted(groups[key], reverse=True)

    list1 = []
    for freqs in groups:
        for number in groups[freqs]:
            for freq in range(freqs):
                list1.append(number)

    return list1


arr1 = [4, 4, 3, 1, 6, 6, 6, 1]  # Output: [3,4,4,1,1,6,6,6]
arr2 = [8, -8, 2, -8, -5, -3]  # Output: [8,2,-3,-5,-8,-8]

print(freq_sort(arr1))
print(freq_sort(arr2))
