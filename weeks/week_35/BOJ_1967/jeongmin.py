import sys
from collections import deque

input = sys.stdin.readline


def bfs(x):
    q = deque()
    q.append(x)
    c = [-1 for _ in range(n+1)]
    c[x] = 0

    while q:
        x = q.popleft()
        for nx, w in graph[x]:
            if c[nx] == -1:
                c[nx] = c[x] + w
                q.append(nx)

    return c


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

tmp = bfs(1)
v = tmp.index(max(tmp))
tmp = bfs(v)
print(max(tmp))