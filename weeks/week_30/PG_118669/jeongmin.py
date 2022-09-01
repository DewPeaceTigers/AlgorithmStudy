import heapq

def solution(n, paths, gates, summits):

    # 인접리스트 저장
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append((w, j))             # 걸리는 시간, 도착지점
        graph[j].append((w, i))
    
    # 산봉우리 오름차순
    summits.sort()
    
    d = [1e9] * (n+1)

    pq = []
    # 모든 출발지를 우선순위 큐에 삽입
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        d[gate] = 0

    # 산봉우리에 도착할 때까지 반복
    while pq:
        intensity, node = heapq.heappop(pq)
        
        # 산봉우리이거나 더 큰 intensity라면 더 이상 이동하지 않음
        if node in summits or intensity > d[node]:
            continue

        # 이번 위치에서 이동할 수 있는 곳으로 이동
        for weight, next_node in graph[node]:
            # next_node 위치에 더 작은 intensity로 도착할 수 있다면 큐에 넣지 않음
            # (출입구는 이미 0으로 세팅되어있기 때문에 방문하지 않음)
            new_intensity = max(intensity, weight)
            if new_intensity < d[next_node]:
                d[next_node] = new_intensity
                heapq.heappush(pq, (new_intensity, next_node))
    
    # 구한 intensity 중 가장 작은 값 반환
    answer = [0, 10000001]
    for summit in summits:
        if d[summit] < answer[1]:
            answer[0] = summit
            answer[1] = d[summit]
            
    return answer