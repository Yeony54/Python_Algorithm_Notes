import sys

def solution(num):
    res = 1
    for n in str(num):
        if n == '1':
            res += 3
        elif n == '0':
            res += 5
        else: res += 4
            
    return res

while 1:
    N = int(sys.stdin.readline())
    if N == 0: break
    print(solution(N))
