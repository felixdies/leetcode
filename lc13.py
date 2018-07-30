def solve(s):
    symb = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    num = (1, 5, 10, 50, 100, 500, 1000)
    ans = 0
    last = -1
    for c in s:
        idx = symb.index(c)
        ans += num[idx]
        if last > -1 and last < idx:
            ans -= 2 * num[last]
        last = idx
    return ans


arr1 = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
result = list(map(solve, arr1))
print(result)
