""" 
다른사람 풀이 
[구현 문제!!]
"""

import sys

def pos(now):
    """
    1. 차이가 1만 경사로 설치 가능
    2. 현재 높이 < 이전 높이, 경사로 설치를 위해 오른쪽 스캔 (낮은 곳에 경사로 설치)
    3. 현재 높이 > 이전 높이, 경사로 설치를 위해 왼쪽 스캔 (낮은 곳에 경사로 설치)
    :param i:
    :return:
    """
    for j in range(1, n):
        if abs(now[j] - now[j - 1]) > 1:   # 1. 차이가 1만 가능
            return False
        if now[j] < now[j - 1]:            # 2.  현재 < 이전, 경사로를 만들기 위해 오른쪽을 스캔함(낮은 곳에 경사로 설치)
            for k in range(l):  # l 만큼 경사로 너비 필요
                if j + k >= n or used[j + k] or now[j] != now[j + k]: # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우, 그만
                    return False
                if now[j] == now[j + k]:   # 높이가 같은 경우 사용 여부 체크
                    used[j + k] = True
        elif now[j] > now[j - 1]:         # 3.  현재 > 이전, 경사로를 만들기 위해 왼쪽을 스캔함
            for k in range(l):
                if j - k - 1 < 0 or now[j - 1] != now[j - k - 1] or used[j - k - 1]:  # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우, 그만
                    return False
                if now[j - 1] == now[j - k - 1]:   # 높이가 같은 경우 사용 여부 체크
                     used[j - k - 1] = True
    return True   # 모두 문제없이 설치된 경우 가능함을 출력

n, l = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0

# 1. 가로 확인
for i in range(n):
    used = [False for _ in range(n)]  # 사용 여부
    if pos(graph[i]):  # 현재 확인할 길을 넣어준다.
        result += 1

# 2. 세로 확인
for i in range(n):
    used = [False for _ in range(n)]
    if pos([graph[j][i] for j in range(n)]):  # 현재 확인할 길을 넣어준다.
        result += 1

print(result)