def solve(str):
    res = ""
    for c in str:
        res += chr(ord(c)+32) if 65 <= ord(c) <= 90 else c
    return res


testCases = ['ab', 'Ab', 'aB', 'c1', 'C1']
result = list(map(solve, testCases))
print(result)
