# 미확인 도착지
# s : 예술가들의 출발지
# g, h : 예술가들이 g와 h 교차로 사이에 있는 도로를 지나감

# 입력에서 주어진 목적지 후보들 중 가능한 목적지들 정렬 (오름차순)

import heapq

INF = float('inf')

T = int(input())

for _ in range(T):
    # 교차로, 도로, 목적지 후보의 개수
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    road = [[] for _ in range(n+1)]

    for _ in range(m):
        # a와 b 사이에 길에 d의 양방향 도로가 있음
        a, b, d = map(int, input().split())
        if (a==g and b==h) or (a==h and b==g):
            d -= 0.1
        road[a].append((b, d))
        road[b].append((a, d))

    dist = [INF] * (n + 1)
    can = [False] * (n + 1)
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        d, b = heapq.heappop(q)

        if dist[b] < d:
            continue

        for r in road[b]:
            # r[0]: 도착지, r[1] : 길이
            if d + r[1] < dist[r[0]]:
                dist[r[0]] = d + r[1]
                heapq.heappush(q, (dist[r[0]], r[0]))

    ans = []
    for _ in range(t):
        # 목적지 후보
        x = int(input())
        if dist[x] != INF and type(dist[x])==float:
            ans.append(x)
    ans.sort()
    print(*ans)