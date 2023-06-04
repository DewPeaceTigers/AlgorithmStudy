from collections import deque
import sys

input = sys.stdin.readline

# 사람의 수 N, 파티의 수 M 입력
N, M = map(int, input().split())

# 진실을 아는지 여부 저장
truth = [False]*(N+1)
# 진실을 아는 사람의 수와 번호
t = list(map(int, input().split()))
for i in range(t[0]):
    truth[t[i+1]] = True

# 연결관계 저장
graph = [[] for _ in range(N+1)]

# 파티에 온 사람 번호 저장
party = []
for _ in range(M):
    p = list(map(int, input().split()))

    people_cnt = p[0]
    people_num = p[1:]
    party.append(people_num)

    for i in people_num:
        for j in people_num:
            if i == j:
                continue

            if j not in graph[i]:
                graph[i].append(j)
# print(graph)

# 진실을 아는 사람과 연결된 모든 사람들은 진실을 안다!
q = deque(t[1:])
while q:
    cur = q.popleft()

    if not truth[cur]:
        continue

    for x in graph[cur]:
        if not truth[x]:
            truth[x] = True
            q.append(x)
# print(truth)

# 과장된 이야기를 할 수 있는 파티의 수
answer = 0
for people in party:
    possible = True

    # 한사람이라도 진실을 알고 있다면 과장된 이야기 불가능
    for p in people:
        if truth[p]:
            possible = False
            break

    if possible:
        answer += 1

print(answer)


"""
처음에 생각하지 못한 반례!!

    6 5
    1 6
    2 4 5
    2 1 2
    2 2 3
    2 3 4
    2 5 6

    -> 0
"""
