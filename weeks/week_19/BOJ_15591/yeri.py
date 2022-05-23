import sys
from collections import defaultdict
input = sys.stdin.readline
INF = int(1e9)

N,Q = map(int,input().split())
maps = defaultdict(list)

for _ in range(N-1):
    p,q,r = map(int,input().split())
    maps[p].append((q,r))
    maps[q].append((p,r))

def dfs(k,v):
    visited=[False]*(N+1)
    stack = [[v,INF]]
    cnt=0
    while stack:
        cur, dist = stack.pop()
        if not visited[cur] and dist >=k:
            visited[cur]=True
            cnt+=1
            stack.extend(maps[cur]) # 연결된 동영상들 확인
    return cnt-1

for _ in range(Q):
    k,v = map(int,input().split()) # 최소 유사도, 현재 보고 있는 동영상
    print(dfs(k,v))

