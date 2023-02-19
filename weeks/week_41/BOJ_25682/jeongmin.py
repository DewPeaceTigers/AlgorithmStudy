### 다른사람 풀이

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0]*M] + [[0] + list(input().strip()) for _ in range(N)]

# 요약 : 맨 처음이 W로 시작하는 "조건 만족 전체 사이즈 체스판"과 B로 시작하는 "조건 만족 전체 사이즈 체스판"을 미리 구해두고,
# 필요 색칠 횟수를 값으로 삼는 누적합을 미리 구해둔 뒤, 그걸 활용하여 체스판을 자르는 모든 경우의 수를 돌면서 최소 색칠 횟수를 구한다.

# 임의의 K*K 크기에서 색칠 횟수를 구할 때 왼쪽 윗 부분에서 한 칸씩 전의 idx를 사용하기 때문에, 편의를 위해 idx의 시작을 1부터로 통일한다.
# check는 모든 칸이 조건을 충족하는 체스판을 나타낸 것이다.
check_W = ["0"*(M+1)] + ["0" + "WB"*(M//2) + "W"*(M%2), "0" + "BW"*(M//2) + "B"*(M%2)]*(N//2) + ["0" + "WB"*(M//2) + "W"*(M%2)]*(N%2)
check_B = ["0"*(M+1)] + ["0" + "BW"*(M//2) + "B"*(M%2), "0" + "WB"*(M//2) + "W"*(M%2)]*(N//2) + ["0" + "BW"*(M//2) + "B"*(M%2)]*(N%2)

# sum_sub는 (1, 1)부터 (x, y)까지의 체스판의 색칠 횟수 값을 담는 2차원 리스트이다.
sum_sub_W = [[0]*(M+1) for _ in range(N+1)]
sum_sub_B = [[0]*(M+1) for _ in range(N+1)]

# 누적합 리스트 완성해놓기
for i in range(1, N+1):
    for j in range(1, M+1):
        sum_sub_W[i][j] = int(board[i][j] != check_W[i][j]) + sum_sub_W[i-1][j] + sum_sub_W[i][j-1] - sum_sub_W[i-1][j-1]
        sum_sub_B[i][j] = int(board[i][j] != check_B[i][j]) + sum_sub_B[i-1][j] + sum_sub_B[i][j-1] - sum_sub_B[i-1][j-1]

# 체스판을 자르는 모든 경우의 수를 돌면서 누적합을 이용하여 가장 적은 색칠 횟수를 찾는다.
result = float("inf")
for x_start in range(1, N-K+2):
    for y_start in range(1, M-K+2):
        x_point = x_start+K-1
        y_point = y_start+K-1
        
        cnt_color_W = sum_sub_W[x_point][y_point] - sum_sub_W[x_start-1][y_point] - sum_sub_W[x_point][y_start-1] + sum_sub_W[x_start-1][y_start-1]
        cnt_color_B = sum_sub_B[x_point][y_point] - sum_sub_B[x_start-1][y_point] - sum_sub_B[x_point][y_start-1] + sum_sub_B[x_start-1][y_start-1]
        
        result = min(result, cnt_color_W, cnt_color_B)

print(result)