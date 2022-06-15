import heapq # 우선순위 큐 사용

def dijkstra(start, graph, dist):
    dist[start]=0
    
    q=[]
    heapq.heappush(q, (0, 1))
    while q:
        cost, v = heapq.heappop(q)
        for g in graph[v]:
            if dist[g[0]] > dist[v]+ g[1]:
                dist[g[0]] = dist[v]+ g[1] 
                heapq.heappush(q, (dist[g[0]], g[0]))
                
    
def solution(n, edge):
    answer = 0
    
    INF = int(1e9)
    
    # 다익스트라 이용
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        a, b = e
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    # 최단 거리 저장 테이블
    dist = [INF]*(n+1)
    
    # 다익스트라 수행
    dijkstra(1, graph, dist)
        
    # 무한대 -1로 변경
    for i in range(n+1):
        if dist[i] == INF:
            dist[i] = -1
    
    # 최댓값 개수 저장
    answer = dist.count(max(dist))
    
    return answer