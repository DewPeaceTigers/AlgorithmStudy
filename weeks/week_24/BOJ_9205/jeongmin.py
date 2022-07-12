from collections import deque

import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(home)

    # 편의점 방문여부 저장
    v = [0] * len(store)
    while q:
        x, y = q.popleft()

        # 페스티벌까지 거리가 1000이하인 경우
        # 두 좌표 사이의 거리는 x좌표의 차이 + y좌표의 차이 (맨허튼 거리)
        if abs(x-rock[0]) + abs(y-rock[1])<=1000:
            return True

        # 편의점 방문
        for i, s in enumerate(store):
            if not v[i] and abs(x-s[0]) + abs(y-s[1])<=1000:
                v[i] = 1
                q.append(s)
    return False


for t in range(int(input())):
    # 맥주를 파는 편의점의 개수
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    rock = list(map(int, input().split()))

    if bfs():
        print("happy")
    else:
        print("sad")

"""
1
2
0 0
-1000 0
1000 0
2000 0
"""