def solve(J, S):
    res = 0
    j = 0
    for s in range(len(S)):
        if S[s] == J[j]: j+=1
        elif S[s] == J[0]: j=1
        else: j=0

        if j == len(J):
            j=0
            res+=1
    return res


jewels = ["aA", "z", "ab"]
stones = ["aAAbbbb", "ZZ", "abab"]
result = list(map(solve, jewels, stones))
print(result)
