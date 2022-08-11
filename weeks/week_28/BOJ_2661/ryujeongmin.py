"""
백트래킹 문제!
길이가 N인 좋은 수열 중 가장 작은 수
- 인접한 부분에는 무조건 다른 수가 나와야 함.
"""

import sys

input = sys.stdin.readline

N = int(input())

s = []
def back_tracking(idx):
    for i in range(1, (idx//2)+1):
        if s[-i:] == s[-2*i:-i]:
            return -1
    if idx == N:
        for i in range(N):
            print(s[i], end='')
        return 0

    for i in range(1, 4):
        s.append(i)
        if back_tracking(idx+1)==0:
            return 0
        s.pop()

back_tracking(0)