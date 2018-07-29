def solve(s):
    dic = {}
    for c in s:
        dic[c] = dic.get(c, 0) + 1

    res = 0
    odd = 0
    for v in dic.values():
        res += v//2
        if v%2: odd = 1

    return odd + (2*res)


arr1 = ["abccccdd"]
result = list(map(solve, arr1))
print(result)