import sys
from collections import defaultdict,deque
input = sys.stdin.readline

N = int(input())
M = int(input())
cities = [list(map(int,input().split())) for _ in range(N)]

plan = list(map(int,input().split()))

graph = defaultdict(list)

for i in range(N):
    for j in range(N):
        if cities[i][j]==1:
            graph[i].append(j)
answer="YES"
for i in range(len(plan)-1):
    start = plan[i]-1
    dest = plan[i+1]-1

    q = deque([start])
    visit=[False]*N
    can = False
    while q:
        s = q.popleft()
        if s==dest:
            can = True
            break
        for next in graph[s]:
            if visit[next]: continue
            visit[next]=True
            q.append(next)
    if not can:
        answer = "NO"
        break
print(answer)