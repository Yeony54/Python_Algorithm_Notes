# BJ 1655 

# 방법
# 들어오는 값 차례로 정렬 (list)
# list 길이가 2 이하일때 list[0] 출력
#   list 길이가 1 일때 제일 작은 list[0] 출력
#   list 길이가 2 일때 외친 수가 짝수개 이기 때문에 중간에 있는 수 중 작은 수인 list[0] 출력
# list 길이가 짝수 일때 list[len(list)//2-1] 를 중간값으로 출력
# list 길이가 홀수 일때 list[len(list)//2] 를 중간값으로 출력

# 어떤 방식의 list 정렬 을 써야하나?

'''
heapq를 사용
left_heap(max heap)과 right_heap(min heap)을 사용하여 자동정렬
heappush()
    L[0]과 비교하여 heappush()
        L[0]보다 작거나 같으면 L에 heappush()
        L[0]보다 크다면 R에 heappush()
    길이를 비교하여 L이 R과 같거나 1 더 길게 맞춘다.
        L과 R의 차이가 2 라면 L에서 heappop()한 값을 R에 heappush()
        L과 R의 차이가 -1 라면 R에서 heappop()한 값을 L에 heappush()
    L[0] return
'''

import sys
import heapq

N = int(sys.stdin.readline())
left_heap = []
right_heap = []

n = int(sys.stdin.readline())
heapq.heappush(left_heap,(-n,n))
print(left_heap[0])

for i in range(1,N):
    n = int(sys.stdin.readline())
    if left_heap[0]>=n :
        heapq.heappush(left_heap,(-n,n))
    else : heapq.heappush(right_heap,n)
    if len(left_heap)-len(right_heap) not in [0,1] :
        if len(left_heap)-len(right_heap)==2 :
            heapq.heappush(right_heap, heapq.heappop(left_heap)[1])
        else : 
            a = heapq.heappop(right_heap)
            heapq.heappush(left_heap, (-a,a))
    print(left_heap[0])


''' 
# 시간초과

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
'''

