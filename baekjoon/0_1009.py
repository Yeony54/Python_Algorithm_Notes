import sys

''' 시간초과
def solution(a, b):
    num = a
    if a == 1:
        return 1
    for i in range(1,b):
        num = int(str(num * a)[-1])
    return num

'''

def solution(a, b):
    
    # 지수를 4로 나눠서 최소의 계산을 할 수 있도록함
    b = b%4        
    if b == 0 : b = 4
    
    # range(1, b) 만큼 지수계산을 함
    # 지수가 1일 때에는 지수계산을 하지 않음
    num = a
    for i in range(1,b):
        
        # 현재 숫자(num)에 a를 곱하여 마지막 숫자를 int로 바꿔서 num에 저장
        num = int(str(num*a)[-1])
    
    # 0번째 컴퓨터는 10번째 컴퓨터를 의미한다.
    return (10 if num==0 else num)
        

N = int(sys.stdin.readline())

for i in range(N):
    num1, num2 = map(int,sys.stdin.readline().split())
    print(solution(num1, num2))