'''
1. 루트 노드에서 가장 먼 노드 찾기
2. 1번에서 가장 먼 노드 찾기
'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
graphs=[[] for _ in range(n+1)]

def dfs(x, cost):
    for i in graphs[x]:
        node, weight=i
        if distance[node]==-1:
            distance[node]=cost+weight
            dfs(node, distance[node])

for _ in range(n-1):
    a, b, c=map(int, input().split())
    graphs[a].append([b, c])
    graphs[b].append([a, c])

distance=[-1]*(n+1)
distance[1]=0
dfs(1, 0)

start=distance.index(max(distance))
distance=[-1]*(n+1)
distance[start]=0
dfs(start, 0)
print(max(distance))