def solution(n, results):
    INF = int(1e9)
    graph = [[INF]*n for _ in range(n)]
    for a,b in results:
        graph[a-1][b-1] =1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j: continue
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    answer = 0
    for i in range(n):
        count = 1
        for j in range(n):
            if i==j: continue
            if graph[i][j] != INF : count+=1
            if graph[j][i] != INF : count+=1
        if count == n : answer+=1
    return answer