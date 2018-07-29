def solve(J, S):
    res = 0
    for s in S:
        if s in J: res+=1
    return res


jewels = ["aA", "z", "ab"]
stones = ["aAAbbbb", "ZZ", "abab"]
result = list(map(solve, jewels, stones))
print(result)
