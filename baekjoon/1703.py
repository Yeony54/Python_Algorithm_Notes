'''
입력의 각 줄은 하나의 branchorama 나무를 의미합니다.

각 줄은 나무의 나이 a(1 ≤ a ≤ 20)로 시작하며, 그 뒤로 2a 개의 정수가 공백을 두고 주어집니다. 2a 개의 정수는 splitting factor와 가지치기 한 가지의 수가 level 별로 나열된 것입니다.

마지막 줄로  '0'이 주어지며 더 이상의 입력은 없습니다. '0'은 처리하지 않습니다.

'''
import sys
while(1):
    tree = list(map(int, sys.stdin.readline().split()))
    if tree == [0] : break
    else :
        def solution(tree):
            N = tree[0]
            t_list = [[tree[i],tree[i+1]] for i in range(1,len(tree[1:]),2)]
            res = 1
            for t in t_list:
                res = res*t[0]-t[1]
            return res

        print(solution(tree))