def solution(n, results):
    INF = int(1e9)
    # 2차원 거리테이블 리스트 초기화
    graph = [[INF] * (n+1) for _ in range(n+1)]
    # 자신의 노드간의 거리는 0으로 변경
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
    # 주어지는 그래프 정보 입력
    for w, l in results: 
        graph[w][l] = 1

    # k=거쳐가는 노드
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    answer=0
    for i in range(1,n+1):
        cnt=0
        for j in range(1,n+1):
            if graph[i][j] != INF and graph[i][j]!=0:
                cnt+=1
            if graph[j][i] != INF and graph[j][i]!=0:
                cnt+=1
        if cnt==n-1: answer+=1
    return answer
