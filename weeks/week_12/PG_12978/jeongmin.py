# 다익스트라 문제!!
# 1번 마을에서 각 마을로 배달을 가는 경우 걸리는 최소 시간 구하기
# K시간 이하로 배달 가능한 마을 개수 구하기
# 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있음!!!
# 임의의 두 마을간에 항상 이동 가능한 경로가 존재함

import heapq

def kruskal(graph, d, INF, N, K):
    # K시간 이하로 배달 가능한 마을 개수 저장 (마을 1 포함하고 시작)
    cnt = 0
    
    q = []
    # 최소힙 사용
    heapq.heappush(q, (0, 1))
    
    while q:
        # 걸리는 시간, 시작 마을
        c, a = heapq.heappop(q)
        
        for g in graph[a]:
            # g[0] : 걸리는 시간, g[1] : 도착 마을
            if d[g[1]] > g[0] + c:
                # 최소로 걸리는 시간 저장
                d[g[1]] = g[0] + c

                # print(a, g[1], d[g[1]])
                
                if d[g[1]] <= K:
                    heapq.heappush(q, (d[g[1]], g[1]))
                # print(q)
                
    for i in range(1, N+1):
        if d[i] <= K: # K시간 이하로 배달 가능한 경우
            cnt += 1
            
    return cnt

def solution(N, road, K):
    answer = 0
    
    INF = 500000
    
    # 도로 정보 저장
    graph = [[] for _ in range(N+1)]
    t = [[INF]*(N+1) for _ in range(N+1)]
    
    # 거리 저장
    d = [INF] * (N+1)
    
    # 첫번째 마을
    d[1] = 0
    
    for r in road:
        # 도로를 연결하는 두 마을 번호 (a, b), 도로는 지나는데 걸리는 시간 (c)
        a, b, c = r
        # 걸리는 시간이 더 짧은 경우로 저장
        if c < t[a][b]:
            t[a][b] = c
            t[b][a] = c
            
            graph[a].append([c, b])
            graph[b].append([c, a])

    answer = kruskal(graph, d, INF, N, K)
    
    return answer