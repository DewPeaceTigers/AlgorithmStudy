"""
두 가지 연산만 가능
1. 문자열의 뒤에 A를 추가한다.
2. 문자열을 뒤집고 뒤에 B를 추가한다.

거꾸로 생각하기!!!
"""

import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

while len(S) != len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[::-1][1:]

print(int(S==T))