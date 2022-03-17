import sys

A, B, C = map(int, sys.stdin.readline().split())

price = A
money = C-B
if money <= 0:
    print(-1) # 노트북을 팔았을 때 수익이 없을 경우 return -1
else :
    # num * money >= price
    # num >= price/money
    # if price%money == 0:
    #     print(price/money)
    # else :
    #     print(price//money + 1)
    print(price//money + 1) # 금액이 0이면 수익이나지 않은것