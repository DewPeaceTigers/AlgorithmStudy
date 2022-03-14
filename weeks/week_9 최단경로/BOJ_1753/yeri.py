"""
다익스트라 알고리즘

"""
import sys
import heapq
input = sys.stdin.readline

V,E=map(int,input().split())
k=int(input())
#graph=[[-1]*V for i in range(V)]
graph=[[] for _ in range(V)]
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u-1].append((v-1,w))
#print(graph)
heap=[(0,k-1)]
distances=[int(1e9)]*V
distances[k-1]=0
def findMin(top):
    #print(top)
    for next_i,next_d in graph[top[1]]:
        #print(next)
        if distances[next_i]>next_d+top[0]:#graph[top[1]][i]+top[0]:
                distances[next_i]=next_d+top[0]
                heapq.heappush(heap,(distances[next_i],next_i))


while heap:
    top=heapq.heappop(heap)
    findMin(top)
for distance in distances:
    if distance==int(1e9): print("INF")
    else: print(distance)

