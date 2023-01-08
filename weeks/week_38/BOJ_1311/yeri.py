import sys
input = sys.stdin.readline
N = int(input())
costs = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1]*(1<<N) for _ in range(N)]

def dfs(depth, visit):
    if depth == N:
        return 0
    if visited[depth][visit] != -1: # 이미 지정이 돼있다면?
        return visited[depth][visit]

    ret = 1000000000
    for i in range(N):
        if (visit&(1<<i)) != 0: # 특정 비트가 켜져있으면
            continue
        ret = min(ret, dfs(depth+1, (visit | (1<<i)) )+ costs[depth][i]) # 가장 작은 거 찾기
    visited[depth][visit] = ret
    return visited[depth][visit]
print(dfs(0,0))