def longestCommonPrefix(strs):
    n = len(strs)
    prefix = strs[0]
    for i in range(1, n):
        if prefix == "":
            break
        temp = ""
        for j in range(min(len(prefix), len(strs[i]))):
            if prefix[j] != strs[i][j]:
                break
            else:
                temp += prefix[j]
        prefix = temp

    return prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))
