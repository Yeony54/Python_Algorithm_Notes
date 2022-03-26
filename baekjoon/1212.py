'''
8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.
'''
import sys
N = int(sys.stdin.readline())
N = str(N)

def solution(N):
    res = []
    for n in N:
        num = int(n)
        for i in range(len(N)):
            res.append(str(num%2))
            num//=2
    return ''.join(res)

print(solution(N))