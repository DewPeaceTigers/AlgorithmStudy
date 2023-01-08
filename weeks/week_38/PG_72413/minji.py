import heapq, sys
INF=sys.maxsize

def solution(n, s, a, b, fares):
    def dijkstra(start):
        visit=[INF for _ in range(n+1)]
        visit[start]=0
        q = []
        heapq.heappush(q, [visit[start], start])
        while q:
            cost, node = heapq.heappop(q)
            for next_node, weight in graph[node] :
                if visit[next_node]>weight+cost :
                    visit[next_node]=weight+cost
                    heapq.heappush(q, [visit[next_node], next_node])
        return visit

    graph=[[] for _ in range(n+1)]
    for i, j, c in fares :
        graph[i].append([j, c])
        graph[j].append([i, c])

    ans=INF
    dist=[[]]
    for i in range(1, n+1):
        dist.append(dijkstra(i))

    for i in range(1, n + 1):
        ans = min(ans, dist[s][i] + dist[i][a] + dist[i][b])

    return ans

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))