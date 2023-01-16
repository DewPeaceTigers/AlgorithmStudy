def solution(n, s, a, b, fares):
    graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
    for c,d,f in fares:
        graph[c][d] = f
        graph[d][c] = f
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    min_dist = int(1e9)
    for passing in range(1,n+1):
        min_dist = min(min_dist, graph[s][passing]+graph[passing][a]+graph[passing][b])
    return min_dist