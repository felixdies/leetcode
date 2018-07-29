""" 매개변수 1개 """
def solve(arg): return 1


arr1 = [1,2,3]
result = list(map(solve, arr1))
print(result)


""" 매개변수 2개 """
def solve(arg1, arg2): return 2


arr1 = [1,2,3]
arr2 = [4,5,6]
result = list(map(solve, arr1, arr2))
print(result)
