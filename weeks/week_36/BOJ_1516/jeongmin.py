# 위상정렬 이용!!
# 먼저 지어야 하는 건물 여러개가 있다고 가정하면, 먼저 지어야하는 건물들 중 최고로 많이 걸리는 시간을 더해주어야 한다

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

# 노드와 간선의 정보 저장한다고 생각하면 됨
building = [[] for _ in range(N + 1)]
# 각 노드의 진입차수 저장
indegree = [0] * (N + 1)
# 건물 짓는데 걸리는 시간
cost = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))[:-1]
    cost[i] = data[0]
    building_data = data[1:]

    # 간선 연결 및 진입차수 설정
    for j in building_data:
        building[j].append(i)
        indegree[i] += 1


# 위상 정렬 함수
def topology_sort():
    result = [0] * (N + 1)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 큐에서 꺼낸 노드 번호에 해당하는 건물을 짓는데 걸리는 시간 저장
        # 선수 건물 짓는데 걸리는 시간이 포함되어 있음!
        # 즉, '선수 건물 짓는데 걸리는 시간 + 현재 건물 짓는데 걸리는 시간'이 저장됨
        result[now] += cost[now]
        for b in building[now]:
            indegree[b] -= 1
            # b번호 건물을 짓기 전에 먼저 지어야하는 선수 건물 짓는데 걸리는 시간으로 갱신
            result[b] = max(result[b], result[now])
            if indegree[b] == 0:
                q.append(b)

    return result


answer = topology_sort()
for i in range(1, N + 1):
    print(answer[i])