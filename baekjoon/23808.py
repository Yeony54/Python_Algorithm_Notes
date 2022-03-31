import sys
N = int(sys.stdin.readline())

for i in range(2*N):
    print('@'*N + ' '*3*N + '@'*N)
for i in range(N):
    print('@'*5*N)
for i in range(N):
    print('@'*N + ' '*3*N + '@'*N)
for i in range(N):
    print('@'*5*N)
        