import sys
from collections import defaultdict,deque
input = sys.stdin.readline

N,M,k = map(int,input().split())

A = list(map(int,input().split()))
graph = defaultdict(list)
for _ in range(M):
    v,w = map(int,input().split())
    graph[v-1].append(w-1)
    graph[w-1].append(v-1)

visit = [False]*N
friends = []

for i in range(N):
    if not visit[i]:
        q = deque([i])
        visit[i] = True
        friend = [A[i]]
        while q:
            now = q.popleft()
            for f in graph[now]:
                if visit[f] : continue
                q.append(f)
                visit[f] = True
                friend.append(A[f])
        friends.append(friend)
all = sum([min(friend) for friend in friends])

if all <=k : print(all)
else: print("Oh no")