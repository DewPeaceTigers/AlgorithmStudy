'''
summits을 set(summits)해줘서 확인하니까 시간초과 해결됨 
'''
import sys
from collections import deque
from collections import defaultdict

INF = sys.maxsize


def bfs(n, graph, gates, summits, distance):
    q = deque(gates)
    while q:
        current = q.popleft()
        if current in summits:
            continue
        for next, cost in graph[current]:
            if distance[next] > max(distance[current], cost):
                q.append(next)
                distance[next] = max(distance[current], cost)
    return distance


def solution(n, paths, gates, summits):
    graph = defaultdict(list)

    for g1, g2, cost in paths:
        graph[g1].append([g2, cost])
        graph[g2].append([g1, cost])

    min_dis = INF
    min_summit = -1
    distance = [INF] * (n + 1)

    for gate in gates:
        distance[gate] = 0

    summit_set = set(summits)
    distance = bfs(n, graph, gates, summit_set, distance)

    for summit in summits:
        if min_dis > distance[summit]:
            min_dis = distance[summit]
            min_summit = summit
        elif min_dis == distance[summit] and min_summit > summit:
            min_summit = summit

    return [min_summit, min_dis]