def solve(str):
    return str.lower()


testCases = ['ab', 'Ab', 'aB']
res = list(map(solve, testCases))
print(res)
