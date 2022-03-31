import sys
N = int(sys.stdin.readline())

for i in range(N):
    print('@'*3*N + ' '*N + '@'*N)
for i in range(3*N):
    print('@'*N + ' '*N + '@'*N + ' '*N + '@'*N)
for i in range(N):
    print('@'*N + ' '*N + '@'*3*N)