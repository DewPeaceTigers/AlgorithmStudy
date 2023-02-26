import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

# 연결 정보 입력
graph = [list(map(int, input().split())) for _ in range(N)]

# 여행 계획 정보 입력
plan = list(map(int, input().split()))

# 도시 방문 여부 저장
visited = [False] * N


def dfs(x):
    for i in range(N):
        # 연결 되어 있는 도시 방문
        if not visited[i] and graph[x][i]:
            visited[i] = True
            dfs(i)


# 여행 계획 중 첫번째 도시에서 출발
start = plan[0]-1
visited[start] = True
dfs(start)


answer = "YES"
# 여행 계획에 있는 도시들을 방문했는지 확인
for i in range(M):
    # 방문하지 못한 도시가 있는 경우 불가능
    if not visited[plan[i]-1]:
        answer = "NO"
        break

print(answer)

"""
5
5
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
5 3 2 3 4
"""