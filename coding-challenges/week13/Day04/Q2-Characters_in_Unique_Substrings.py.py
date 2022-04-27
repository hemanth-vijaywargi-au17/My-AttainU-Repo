def uniqueLetterString(S):
    sums = [1] * len(S)
    for i in range(1, len(S)):
        sums[i] += sums[i - 1]
    res = 0
    prev = {}
    lsum = 0
    for i, s in enumerate(S):
        lsum = lsum + sums[i]
        res += lsum
        ip = prev.get(s, None)
        if ip is None:
            prev[s] = [i, None]
        elif ip[1] is None:
            ip[1] = i
            res -= 2 * (len(sums) - i) * (ip[0] + 1)
        else:
            res -= (len(sums) - i) * (ip[0] + 1)
            res -= 2 * (len(sums) - i) * (ip[1] - ip[0])
            ip[0] = ip[1]
            ip[1] = i
    return res


if __name__ == "__main__":
    S = "ABA"
    print(uniqueLetterString(S))
