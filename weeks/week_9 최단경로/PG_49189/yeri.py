import heapq
def solution(n, edge):
    graph=[[] for _ in range(n)]

    for a,b in edge:
        graph[a-1].append((b-1,1))
        graph[b-1].append((a-1,1))
    heap=[(0,0)] # cost 먼저
    INF=50001
    distances=[INF]*n
    distances[0]=0
    while heap:
        cost,idx = heapq.heappop(heap)
        for next_i,next_d in graph[idx]:
            if distances[next_i] > next_d+cost:
                distances[next_i]=next_d+cost
                heapq.heappush(heap,(distances[next_i],next_i))
    return distances.count(max(distances))