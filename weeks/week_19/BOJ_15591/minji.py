'''
틀림
'''
from collections import deque

n, q=map(int, input().split())
graph=[[] for _ in range(n+1)]

for _ in range(n-1) :
    p, q, r=map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

def bfs(k, v) :
    visit = [0] * (n + 1)
    ans = 0
    q = deque()
    q.append([v, float('inf')])

    while q:
        v, usado = q.pop()
        visit[v]=1
        for next_v, next_usado in graph[v]:
            if next_usado >= k and visit[next_v] == 0:
                visit[next_v] = 1
                if next_usado >= usado :
                    q.append([next_v, usado])
                    ans+=1
                elif next_usado >=k :
                    q.append([next_v, next_usado])
                    ans+=1

    return ans

for _ in range(q):
    k , v=map(int, input().split())
    print(bfs(k, v))

