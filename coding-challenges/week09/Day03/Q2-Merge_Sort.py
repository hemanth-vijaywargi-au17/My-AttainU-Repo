"""
Q-2 ) Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
"""

# Question wants to modify nums1 in-place instead of returning a new merged list
# So merge_sort has been modified to do this

def merge(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    A = nums1[:n - m]
    n1 = len(A)
    p1 = 0
    p2 = 0
    i = 0

    while p1 < n1 and p2 < m:
        if A[p1] < nums2[p2]:
            nums1[i] = A[p1]
            i += 1
            p1 += 1
        else:
            nums1[i] = nums2[p2]
            i += 1
            p2 += 1

    while p1 < n1:
        nums1[i] = A[p1]
        i += 1
        p1 += 1

    while p2 < m:
        nums1[i] = nums2[p2]
        i += 1
        p2 += 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

merge(nums1, nums2)

print(nums1)
