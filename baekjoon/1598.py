import sys

A, B = map(int, sys.stdin.readline().split())

def solution (A, B):
    A, B = A-1, B-1
    v = abs(A%4 - B%4)
    h = abs(A//4 - B//4)
    return (v+h)

print(solution(A, B))