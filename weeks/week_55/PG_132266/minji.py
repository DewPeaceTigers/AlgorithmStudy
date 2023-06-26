import heapq


def solution(n, roads, sources, destination):
    answer = []
    maps = [[] for _ in range(n + 1)]

    for a, b in roads:
        maps[a].append(b)
        maps[b].append(a)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        visit = [float('inf')] * (n + 1)
        visit[start] = 0

        while q:
            cost, now = heapq.heappop(q)
            for i in maps[now]:
                if visit[i] > cost + 1:
                    visit[i] = cost + 1
                    heapq.heappush(q, (cost + 1, i))
        return visit

    result = dijkstra(destination)
    for source in sources:
        if result[source] == float('inf'):
            answer.append(-1)
        else:
            answer.append(result[source])

    return answer