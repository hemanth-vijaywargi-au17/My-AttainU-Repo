def common_prefix(strs):
    n = len(strs)
    prefix = ""
    mini = len(strs[0])
    for i in strs:
        if len(i) < mini:
            mini = len(i)

    for j in range(mini):
        common = True
        for i in range(n - 1):
            if strs[i][j] != strs[i + 1][j]:
                common = False
                break
        if common:
            prefix += strs[0][j]
        else:
            break

    return prefix


strs = ["flower", "flow", "flight"]
print(common_prefix(strs))

# Another Approach
# def common_prefix2(strs):
#     n = len(strs)
#     prefix = strs[0]
#     for i in range(1, n):
#         if prefix == "":
#             break
#         temp = ""
#         for j in range(min(len(prefix), len(strs[i]))):
#             if prefix[j] != strs[i][j]:
#                 break
#             else:
#                 temp += prefix[j]
#         prefix = temp
#     return prefix
