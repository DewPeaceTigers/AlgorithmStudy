import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

# 유사도 저장
graph = [[] for _ in range(N+1)]

# 두 동영상 쌍의 USADO 입력
for _ in range(N-1):
    p, q, r = map(int, input().split())

    graph[p].append((q, r))
    graph[q].append((p, r))

# 임의의 두 쌍 사이의 USADO 구하기
# 경로의 모든 연결들의 USADO 중 최솟값
for _ in range(Q):
    k, v = map(int, input().split())

    # print("정점 ", v)
    q = deque()
    q.append((v, 1e9))

    visited = [0] * (N+1)
    visited[v] = 1

    cnt = 0
    while q:
        x, u = q.popleft()

        # USADO가 K 이상인 모든 동영상 추천
        for to, w in graph[x]:
            # print("연결 동영상", to, w)
            next = min(w, u)

            if next >= k and visited[to] == 0:
                cnt += 1
                visited[to] = 1
                q.append((to, min(w, u)))

    print(cnt)
