def list_to_dict(arr):
    dict1 = dict()
    for i in range(len(arr)):
        if arr[i] not in dict1:
            dict1[arr[i]] = 1
        else:
            dict1[arr[i]] += 1
    return dict1


def intersect(nums1, nums2):
    dict2 = list_to_dict(nums2)
    res = []
    for key in nums1:
        if key in dict2 and dict2[key] > 0:
            res.append(key)
            dict2[key] -= 1
    return res


nums1 = [4, 9, 9, 5]
nums2 = [9, 4, 9, 8, 4]

print(intersect(nums1, nums2))
