def solve(s):
    dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    ans = 0
    last = 99999
    for c in s:
        num = dic[c]
        ans += num
        if last < num:
            ans -= 2*last
        last = num
    return ans


arr1 = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
result = list(map(solve, arr1))
print(result)
