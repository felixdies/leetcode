def solve(s):
    import collections
    ans = 0
    for v in collections.Counter(s).values():
        ans += v // 2 * 2
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1
    return ans


arr1 = ["abccccdd"]
result = list(map(solve, arr1))
print(result)