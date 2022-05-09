import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
T = int(input())
def dij(start):
    distance = [int(1e9)]*(n+1)

    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q :
        dist, node = heapq.heappop(q)
        if distance[node] < dist: continue
        for next,n_dist in graph[node]:
            cost = distance[node]+n_dist
            if cost < distance[next]:
                distance[next]=cost
                heapq.heappush(q,(cost,next))
    return distance
for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a,b,d=map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    cands=[]
    for _ in range(t):
        cands.append(int(input()))
    s_ = dij(s)
    g_ = dij(g)
    h_ = dij(h)
    answer=[]
    for cand in cands:
        if s_[cand] == s_[g]+g_[h]+h_[cand] or s_[cand] == s_[h]+h_[g]+g_[cand]:
            answer.append(cand)
    print(*sorted(answer))
