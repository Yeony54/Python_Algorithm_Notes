'''
창영이는 심심해서 혼자 재미 없는 게임을 하나 생각해냈다. 
숫자 N을 먼저 정하고, 이 숫자를 2진법, 3진법, 4진법, ..., 100만진법, 100만 1진법 등등으로 바꾸어 보면서, 
마지막자리에 연속된 0의 개수를 모두 더하는 것이다.

예를 들어 N=5라면, 2진법 101, 3진법 12, 4진법 11, 5진법 10, 6진법 5, 7진법 5, ... 
등과 같으므로 답은 1이 된다. 여러분이 할 일은 주어진 N에 대해서 창영이가 구한 답을 찾는 것이다.

'''


import sys
N_list = list(map(int,sys.stdin.readline().split()))

N = N_list[0]
b_list = N_list[1:]

def solution(N, b_list):
    for b in b_list:
        res = {1,b}
        if b%2 == 0 : 
            res.add(2)
            res.add(b//2)
        for i in range(3, int(b**1/2)+1, 2):
            if b%i == 0:
                res.add(i)
                res.add(b//i)
        print(res) ## 지워줘야행
        print(len(res)-1)

solution(N, b_list)

# def solution(N, b_list):
#     for b in b_list:
#         res = 1
#         if b == 1 : print(0)
#         elif b == 2 : print(1)
#         elif b == 3 : print(1)
#         elif b == 4 : print(2)
#         else:
#             # 제곱수이면 +1
#             if b**(1/2) == int(b**(1/2)) : res += 1 
#             if b%2 == 0 : res += 1
#             # 제곱근 수보다작은수까지 카운트 *2
#             for i in range(3,int(b**(1/2))+1, 2):
#                 if b%i == 0 : res += 2     
#             print(res)
