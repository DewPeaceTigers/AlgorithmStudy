import heapq
from collections import deque

# 다익스트라 수행
def dijkstra(start, dp, graph):
    
    q = []
    heapq.heappush(q, (0, start))
    dp[start][start] = 0
    
    while q:
        cost, now = heapq.heappop(q)
        
        # 방문했던 지점인지
        if dp[start][now] < cost:
            continue
        
        # x에서 최저 요금으로 갈 수 있는 지점으로 이동
        for to, x in graph[now]:
            fare = cost + x
            
            if fare < dp[start][to]:
                dp[start][to] = fare
                heapq.heappush(q, (dp[start][to], to))

def solution(n, s, a, b, fares):
    answer = 1e9
    
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        # (비용, 도착지점) 
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    # 최저 요금 테이블
    dp = [[1e9] * (n+1) for _ in range(n+1)]
    
    # (1~n)번 지점에서 a, b로 가는 최저 요금 구하기
    for start in range(1, n+1):
        dijkstra(start, dp, graph)
    
    # 최저 요금 구하기
    # (s->i) + (i->a) + (i->b)
    for i in range(1, n+1):
        answer = min(answer, dp[s][i] + dp[i][a] + dp[i][b])
    
    return answer