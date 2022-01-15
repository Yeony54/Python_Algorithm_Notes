# BJ 1655 

# 방법
# 들어오는 값 차례로 정렬 (list)
# list 길이가 2 이하일때 list[0] 출력
#   list 길이가 1 일때 제일 작은 list[0] 출력
#   list 길이가 2 일때 외친 수가 짝수개 이기 때문에 중간에 있는 수 중 작은 수인 list[0] 출력
# list 길이가 짝수 일때 list[len(list)//2-1] 를 중간값으로 출력
# list 길이가 홀수 일때 list[len(list)//2] 를 중간값으로 출력

# list 정렬을 어떻게 할지 모르겠음

import sys

N = int(sys.stdin.readline())
list = []

for i in range(N):
    n = int(sys.stdin.readline())
    list.append(n)
    if len(list)>2:
        list.sort()
        if len(list)%2==0:
            print(list[len(list)//2-1])
        else : print(list[len(list)//2])
    else :
        list.sort()
        print(list[0])

    print(f'list = {list}')
    