# 최소, 최대
'''
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
'''

import sys

N = int(sys.stdin.readline())
nums = list(map(int, input().split()))
# for i in range(N) :
#     nums.append(int(sys.stdin.readline()))
print(min(nums), max(nums))

