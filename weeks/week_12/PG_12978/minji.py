import heapq
import sys

INF = sys.maxsize


def dijkstra(distance, graph):
    queue = []
    heapq.heappush(queue, [0, 1])

    while queue:
        wei, node = heapq.heappop(queue)

        for next_wei, next_node in graph[node]:
            if wei + next_wei < distance[next_node]:
                distance[next_node] = next_wei + wei
                heapq.heappush(queue, [next_wei + wei, next_node])


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    distance[1] = 0

    for r in road:
        graph[r[0]].append([r[2], r[1]])
        graph[r[1]].append([r[2], r[0]])

    dijkstra(distance, graph)

    return len([x for x in distance if x <= K])