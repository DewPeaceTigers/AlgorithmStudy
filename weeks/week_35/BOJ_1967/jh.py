from collections import defaultdict
import heapq
n=int(input())
graph=defaultdict(list)
for _ in range(n-1):
    start,end,weight=list(map(int,input().split()))
    graph[start].append((end,weight))
    graph[end].append((start, weight))

def check(root):
    Q=[(0,root)]
    dist=defaultdict(int)
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node]=time
            for v,w in graph[node]:
                alt=time+w
                heapq.heappush(Q,(alt,v))
    return dist
dist=check(1)
n1=sorted(dist.items(),key=lambda x:-x[1])[0][0]
dist=check(n1)
n2=sorted(dist.items(),key=lambda x:-x[1])[0][0]
answer = sorted(dist.items(),key=lambda x:-x[1])[0][1]
print(answer)