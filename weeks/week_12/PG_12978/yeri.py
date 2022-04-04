def find_small(visited, distance):
    min_value=int(1e9)
    idx=0
    for i in range(len(visited)):
        if not visited[i] and min_value > distance[i]:
            # 방문하지 않은 노드 중 거리가 가장 작은거
            min_value = distance[i]
            idx=i
    return idx
def solution(N, road, K):
    INF = int(1e9)
    answer=0
    graph=[[INF]*N for _ in range(N)]
    visited=[False]*N # 방문 처리 기록용
    distance=[INF]*N # 거리 테이블용
    for a,b,c in road:
        graph[a-1][b-1]=min(graph[a-1][b-1],c)
        graph[b-1][a-1]=min(graph[b-1][a-1],c)

    distance[0]=0
    visited[0]=True

    # 시작 노드의 인접 노드에 대해 최단 거리 계산
    for i in range(len(graph[0])):
        if graph[0][i]==INF: continue
        distance[i]=graph[0][i]

    for _ in range(N):
        now = find_small(visited,distance) # 현재 거리에서 가장 작은 거 고르기
        visited[now]=True

        # 해당 노드의 인접한 노드들 간의 거리 계산
        for i in range(len(graph[now])):
            if graph[now][i]==INF: continue
            cost = distance[now]+graph[now][i]
            if cost < distance[i]: # 지금 거리보다 짧을 때만
                distance[i]=cost
    for i in range(N):
        if distance[i]<K+1: answer+=1
    return answer