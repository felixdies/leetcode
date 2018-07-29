def solve(arg): return 1
# 매개변수 1개
arr1 = [1,2,3]
result = list(map(solve, arr1))
print(result)


def solve(arg1, arg2): return 2
# 매개변수 2개
arr1 = [1,2,3]
arr2 = [4,5,6]
result = list(map(solve, arr1, arr2))
print(result)
