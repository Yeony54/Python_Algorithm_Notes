'''
baekjoon > 12840

창용이는 여름을 맞이하여 ‘정창용’ 이름이 쓰인 한정판 섬머 에디션 시계를 구입했다. 왠지 오늘은 001도 가고 싶지 않고 시계를 가지고 놀고만 싶다. 우린 방에 있는 창용이가 시계를 가지고 뭘 하는지 궁금하기만 하다. 창용이는 시계의 건전지를 분리했기 때문에 시계는 시간이 흐르지 않는다.

창용이는 앞으로 시계를 돌리기도 하고 뒤로 시계를 돌리기도 한다. 입력으로는 초기 현재 시간이 주어지고 q개의 쿼리가 주어진다.

한 쿼리는 T로 시작한다. (1 ≤ T ≤ 3, 0 ≤ c ≤ 10,000,000)

T가 1일 때는 c를 입력으로 받아와서, 시계를 앞으로 c초 돌린다.
T가 2일 때는 c를 입력으로 받아와서, 시계를 뒤로 c초 돌린다.
T가 3일 때는 창용이가 조작한 시계의 상황을 출력한다.

'''

import sys

h, m, s = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

def solution(N, h, m, s):
    sec = h*3600 + m*60 + s
    read_in = []
    for i in range(N):
        read_in = list(map(int, sys.stdin.readline().split()))
        if read_in[0] == 3:
            print(sec//3600, (sec%3600)//60, (sec%60))
        elif read_in[0] == 1:
            sec += read_in[1]
            sec = sec%86400
        else:
            sec -= read_in[1]
            sec = sec%86400

solution(N, h, m, s)
