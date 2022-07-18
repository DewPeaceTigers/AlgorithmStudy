import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

n1, n2 = map(int, input().split())

graph = [[] for i in range(n+1)]
for i in range(int(input())):
    x1, x2 = map(int, input().split())
    graph[x1].append(x2)
    graph[x2].append(x1)

q = deque()
q.append(n1)

info = [101]*(n+1)
info[n1] = 0
while q:
    x = q.popleft()

    if x == n2:
        break

    for g in graph[x]:
        if info[g] == 101:
            info[g] = info[x]+1
            q.append(g)

answer = -1 if info[n2]==101 else info[n2]
print(answer)