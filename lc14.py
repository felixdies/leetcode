def solve(strs):
    if not strs: return ""

    minlen = len(strs[0])
    for s in strs:
        minlen = min(minlen, len(s))

    for idx in range(minlen):
        same = True
        last = strs[0][idx]
        for s in strs:
            if s[idx] is not last:
                same = False
                break
        if not same:
            return s[:idx]
    return strs[0][:minlen]


arr1 = [["flower","flow","flight"], ["dog","racecar","car"]]
result = list(map(solve, arr1))
print(result)