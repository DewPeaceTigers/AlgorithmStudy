"""
[다른사람 풀이!] 비트마스킹 + DP

| 특정 비트를 킬때 사용 ( x |= (1 << 2))
& 특정비트가 켜져있는지 혹은 특정 비트를 끌 때 사용 (x & (1 << 2)) != 0 or (x & ~(1 << 2)
^ 특정 비트 상태를 반전시킬 때 사용 (x ^ (1 << 2))
tip) x & (-x) x의 제일 오른쪽 1이 나온다.
"""

import sys

input = sys.stdin.readline


def dfs(row, visit):
    if row == N:
        return 0

    if visited[row][visit] != -1:
        return visited[row][visit]

    ret = 1000000000
    for i in range(N):
        if (visit & (1 << i)) != 0:  # 특정 비트가 켜저있다면
            continue

        ret = min(ret, dfs(row + 1, (visit | (1 << i))) + tasks[row][i])

    visited[row][visit] = ret

    return visited[row][visit]


N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * (1 << N) for _ in range(N)]
print(dfs(0, 0))