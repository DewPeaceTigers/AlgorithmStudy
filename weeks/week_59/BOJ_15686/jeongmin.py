from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 도시의 정보 입력
city = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 정보 저장
chicken = []
home = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
            # city[i][j] = 0  # 빈칸으로 변경
        elif city[i][j] == 1:
            home.append((i, j))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 도시의 치킨거리 최솟값 구하기
answer = 1e9

# 치킨집 중에 M개 선택
for case in combinations(chicken, M):

    # 치킨 거리 계산
    city_dist = 0

    # 집과 치킨집 사이 거리 계산
    for hx, hy in home:
        chicken_dist = 1e9
        # case에 담긴 치킨집 표시
        for cx, cy in case:
            dist = abs(hx-cx) + abs(hy-cy)
            chicken_dist = min(chicken_dist, dist)

        city_dist += chicken_dist

    answer = min(answer, city_dist)

print(answer)


"""
# Python3 시간 초과 풀이
# 큐를 사용해서 (행, 열, 거리)를 저장한 후 bfs 돌려서 치킨거리를 구하면 시간초과 뜸..
# (PyPy로 제출하면 통과는 하는데 시간이 거의 4배 걸림)
"""

# from itertools import combinations
# from collections import deque
# import sys

# input = sys.stdin.readline

# N, M = map(int, input().split())

# # 도시의 정보 입력
# city = [list(map(int, input().split())) for _ in range(N)]

# # 치킨집 정보 저장
# chicken = []
# home_cnt = 0
# for i in range(N):
#     for j in range(N):
#         if city[i][j] == 2:
#             chicken.append((i, j))
#             city[i][j] = 0  # 빈칸으로 변경
#         elif city[i][j] == 1:
#             home_cnt += 1

# # 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 도시의 치킨거리 최솟값 구하기
# answer = 1e9

# # 치킨집 중에 M개 선택
# for case in combinations(chicken, M):
#     dist = [[1e9]*N for i in range(N)]
#     visited = [[False]*N for _ in range(N)]
#     home = home_cnt

#     q = deque()
#     # case에 담긴 치킨집 표시
#     for r, c in case:
#         q.append((r, c))  # (행 위치, 열 위치, 거리)
#         visited[r][c] = True
#         dist[r][c] = 0

#     # 치킨 거리 계산
#     chicken_dist = 0
#     while q:
#         x, y = q.popleft()

#         if home <= 0:
#             continue

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # print(nx, ny)

#             # 경계 확인, 방문 체크
#             if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
#                 continue

#             dist[nx][ny] = dist[x][y] + 1

#             # 도시인 경우
#             if city[nx][ny] == 1:
#                 chicken_dist += dist[nx][ny]
#                 if chicken_dist > answer:
#                     break
#                 home -= 1

#             visited[nx][ny] = True
#             q.append((nx, ny))

#     answer = min(answer, chicken_dist)

# print(answer)
