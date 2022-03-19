import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

y_sum = 0
m_sum = 0

for call in arr:
    y_sum += (call+30)//30
    m_sum += (call+60)//60
ys = y_sum*10
ms = m_sum*15

print(f'Y {ys}' if ys<ms  else f'Y M {ms}'if ys==ms  else f'M {ms}')