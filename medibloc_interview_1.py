"""
2018.07.30
메디블록 코딩 인터뷰 1번 문제
홀수 마방진 그리기

인터뷰 때에는 checkEdge(), next() 함수를 분리 하지 않고
하나의 스크립트로 짜려고 시도하면서 긴 시간을 소요했고,
결과 코드도 깔끔하지 못했음.
"""

W = 11
H = 11

ans = [[0]*W for x in range(H)]


def checkEdge(i,j):
    if i==-1: i=H-1
    if j==W: j=0
    return (i,j)


def next(i,j):
    ni=i-1
    nj=j+1
    (ni, nj) = checkEdge(ni, nj)

    if ans[ni][nj] != 0:
        return checkEdge(i, j-1)
    else:
        return (ni, nj)


i=H//2
j=W-1
num=1
while num<=W*H:
    ans[i][j] = num
    i, j = next(i, j)
    num += 1

for a in ans: print(sum(a))

for a in ans:
    print(a)