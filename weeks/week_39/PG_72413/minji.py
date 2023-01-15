import heapq, sys

INF=sys.maxsize

def solution(n, s, a, b, fares):
    def dijkstra(start) :
        distance=[INF]*(n+1)
        distance[start]=0
        q=[]
        heapq.heappush(q, [0, start])
        while q :
            cost, node=heapq.heappop(q)
            for next_node, weight in graph[node]:
                if distance[next_node]>weight+cost:
                    distance[next_node]=weight+cost
                    heapq.heappush(q, [weight+cost, next_node])
        return distance
    graph=[[] for _ in range(n+1)]
    for i, j, c in fares :
        graph[i].append([j, c])
        graph[j].append([i, c])

    ans=INF
    dist=[[]]
    for i in range(1, n+1):
        dist.append(dijkstra(i))
    for i in range(1, n+1) :
        ans=min(ans, dist[s][i]+dist[i][a]+dist[i][b])

    return ans
