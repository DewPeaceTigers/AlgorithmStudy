import sys
input= sys.stdin.readline
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b): # 매개변수 : graph, a(행), b(열)
    queue = deque()
    queue.append((a,b)) # 행, 열 큐에 저장
    graph[a][b] = 0 # 값을 1로 변경 -> visited 변수 사용 안해도 됨

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1 # 배추 위치 1로 저장

		# 그래프의 각 칸을 돌다가 1인 칸을 발견하면 BFS를 수행
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)