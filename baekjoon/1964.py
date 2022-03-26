import sys

def solution(N):
    if N == 0: return 0
    return int((N*5) +  (N*(N-1)/2)*3-(N-1))%45678

N = int(sys.stdin.readline())
print(solution(N))