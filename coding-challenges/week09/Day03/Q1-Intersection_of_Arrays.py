"""
Q-1 ) Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/submissions/
"""


def intersection1(A, B):
    return set(A) & set(B)


def intersection2(A, B):
    return set(A).intersection(B)


def intersection3(A, B):
    A = set(A)
    B = set(B)
    c = []
    for i in A:
        if i in B:
            c.append(i)
    return c


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(list(intersection1(nums1, nums2)))
print(list(intersection2(nums1, nums2)))
print(list(intersection3(nums1, nums2)))
