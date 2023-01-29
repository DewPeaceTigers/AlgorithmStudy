from collections import deque
import sys

sys = sys.stdin.readline

# 유저의 수 N (2 ≤ N ≤ 100), 친구 관계의 수 M(1 ≤ M ≤ 5,000)
N, M = map(int, input().split())

# 친구 관계 입력
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())

    # A와 B 친구, B와 A 친구
    graph[A].append(B)
    graph[B].append(A)

# 케빈 베이컨의 수가 가장 작은 사람 번호
answer = 0
# 케빈 베이컨의 수 최소값 저장
min_bacon_cnt = float('inf')

# 케인 베이컨의 수 구하기 (BFS 수행)
for user in range(1, N+1):
    # 단계 저장
    d = [0] * (N+1)
    # 방문 여부 저장
    visited = [False] * (N+1)
    visited[user] = True

    q = deque()
    q.append(user)
    while q:
        cur = q.popleft()

        for x in graph[cur]:
            # 방문 했던 곳이라면 넘어감
            if visited[x]:
                continue

            # 단계 저장 후 방문 처리
            d[x] = d[cur] + 1
            visited[x] = True
            q.append(x)

    bacon_cnt = sum(d)

    # 케빈 베이컨의 수가 더 작다면 번호 업데이트
    if min_bacon_cnt > bacon_cnt:
        answer = user
        min_bacon_cnt = bacon_cnt

print(answer)