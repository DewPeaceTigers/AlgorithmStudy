"""
1->A->B->N
1->B->A->N
위 두 루트를 계산해 비교하여 작은 경로 출력
"""
import sys, heapq
input = sys.stdin.readline
INF=sys.maxsize

N,E=map(int,input().split())

#graph=[[-1]*V for i in range(V)]
graph=[[] for _ in range(N)]
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u-1].append((v-1,w))
    graph[v-1].append((u-1,w))
a,b=map(int,input().split())
#print(graph)
def findMin(start,end):
    heap=[(0,start)]
    distances=[INF]*N
    distances[start]=0
    while heap:
        cost,idx = heapq.heappop(heap)
        for next_i,next_d in graph[idx]:
            if distances[next_i]>next_d+cost:#graph[top[1]][i]+top[0]:
                    distances[next_i]=next_d+cost
                    heapq.heappush(heap,(distances[next_i],next_i))

    return distances[end]
A2B=findMin(a-1,b-1)
A_first=findMin(0,a-1)+A2B+findMin(b-1,N-1)
B_first=findMin(0,b-1)+A2B+findMin(a-1,N-1)
print(A_first,B_first,INF)
if A_first<=B_first and A_first<INF:
    print(A_first)
elif B_first<A_first and B_first<INF:
    print(B_first)
else:
    print(-1)