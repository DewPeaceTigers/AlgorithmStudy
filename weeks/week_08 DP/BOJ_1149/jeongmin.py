'''[풀이]
규칙: 같은 색이 두번 연속 나오면 안된다!!
'''

import sys
input= sys.stdin.readline

# 집의 수 N(2 ≤ N ≤ 1,000) 입력
N = int(input())

# 각 집을 빨강, 초록, 파랑으로 칠하는 비용 입력
cost= [list(map(int, input().split())) for _ in range(N)]

# 이웃한 집은 다른 색깔로 칠하도록
color =[[1, 2], [0, 2], [0, 1]]

# 집을 칠하는 비용의 최솟값 저장
ans = [[0]*3 for _ in range(N)]

ans[0] = cost[0] 
for i in range(1, N):
  for j in range(3):
    # 현재 색으로 칠하는 비용 + 그 전 집에서 다른 색으로 칠한 비용 중 최솟값 
    ans[i][j]= cost[i][j]+min(ans[i-1][color[j][0]], ans[i-1][color[j][1]])        

# print(ans)
print(min(ans[N-1]))