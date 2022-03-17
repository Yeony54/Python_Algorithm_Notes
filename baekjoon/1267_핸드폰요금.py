import sys
import numpy as np

while(1):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    calls = np.array(arr)
    ys = (calls + 31)//30
    ys = ys.sum() * 10
    ms = (calls + 61)//60
    ms = ms.sum() * 15

    print(f'Y {ys}' if ys<ms  else  f'Y M {ms}' if ys==ms  else f'M {ms}' )