# [23.02.02] 21:08~

# 진실 or 엄청 과장
# 되도록이면 과장해서 이야기함

# 거짓말을 피해야 하는 경우 (진실을 이야기 해야하는 경우)
# - 이야기의 진실을 아는 사람
# - 다른 파티에서 진실을 이야기한 사람인 경우

# 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램

import sys

from collections import defaultdict, deque

# 사람의 수 N, 파티의 수 M
N, M = map(int, input().split())

# 이야기의 진실을 아는 사람의 수와 번호
truth = input()

# 파티별 사람 정보
parties = []
# 사람별 파티 정보
people = defaultdict(list)

for i in range(M):
    party = list(map(int, input().split()))

    cnt, p_nums = party[0], party[1:]
    parties.append(p_nums)

    for x in p_nums:
        people[x].append(i)

# 과장된 이야기를 할 수 있는 파티 개수의 최댓값
answer = M

# 진실을 아는 사람이 없는 경우
if truth[0] == '0':
    print(answer)

else:
    # 파티 확인 여부
    visited_party = [False] * M

    # 사람 방문 여부
    visited_people = [False] * (N+1)

    # 진실을 아는 사람 변호
    truth_nums = list(map(int, truth.split()))[1:]
    q = deque(truth_nums)

    # 진실을 아는 사람이 간 파티는 진실을 이야기 함
    while q:
        num = q.popleft()

        if visited_people[num]:
            continue

        visited_people[num] = True

        for p in people[num]:
            # 진실을 이야기하는 파티
            if visited_party[p]:
                continue
            
            answer -= 1
            visited_party[p] = True
            q.extend(parties[p])

    print(answer)


### 다른 사람 풀이
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# knowList = set(input().split()[1:])
# parties = []

# for _ in range(m):
#     parties.append(set(input().split()[1:]))

# for _ in range(m):
#     for party in parties:
#         if party & knowList:
#             knowList = knowList.union(party)

# cnt = 0
# for party in parties:
#     if party & knowList:
#         continue
#     cnt += 1

# print(cnt)