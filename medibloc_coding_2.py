"""
2018.07.30
메디블록 코딩 인터뷰 2번 문제
합이 100이 되는 연산 찾기

1~9 의 숫자가 순서대로 주어진다.
+,-,붙여쓰기 3가지 방법을 사용하여 합이 100 이 되는 연산을 모두 출력하시오.
"""

def plus(num, pend, sum, ans):
    sum += pend
    ans += "%+d" % pend
    pend = num
    recur(num+1, pend, sum, ans)

def minus(num, pend, sum, ans):
    sum += pend
    ans += "%+d" % pend
    pend = -num
    recur(num+1, pend, sum, ans)

def append(num, pend, sum, ans):
    if pend<0:
        pend = pend*10-num
    else:
        pend = pend*10+num
    recur(num+1, pend, sum, ans)

def recur(num, pend, sum, ans):
    if num==10:
        sum += pend
        ans += "%+d" % pend
        if sum==100:
            print(ans[1:])
        return

    plus(num, pend, sum, ans)
    minus(num, pend, sum, ans)
    append(num, pend, sum, ans)

recur(2, 1, 0, "")
