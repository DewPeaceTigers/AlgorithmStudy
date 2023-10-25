# 위상정렬을 사용해야함!
# 순서가 정해져 있는 일련의 작업을 차례로 수행해야 할 때 사용할 수 있는 알고리즘

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 진입차수 0으로 초기화
indegree = [0]*(N+1)

graph = [[] for _ in range(N+1)]

# 학생 키 비교 정보
for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    indegree[b] += 1

q = deque()
# 진입차수가 0인 것부터 시작
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

# 키 순서대로 학생 번호 저장
result = []
while q:
    now = q.popleft()
    result.append(now)

    for x in graph[now]:
        # 진입차수 -1 처리
        indegree[x] -= 1
        # 진입차수가 0이라면 큐에 추가
        if indegree[x] == 0:
            q.append(x)

print(*result)
