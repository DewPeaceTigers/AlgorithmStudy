''' [풀이]
1. 가능한 체스판 (2가지) 문자열로 저장
2. 8*8 크기로 고르는 모든 경우 확인
    - str 변수에 8*8 보드판 데이터 문자열로 저장
3. (0~63) 반복문 돌면서 체스판이랑 보드판 데이터 비교 
    - c_1, c_2 비교하여 더 작은 값 check 리스트에 저장
4. check 리스트 중 최솟값 출력
'''

import sys
input = sys.stdin.readline

# N과 M(8 ≤ N, M ≤ 50) 입력
N, M = map(int, input().split())

# 가능한 체스판 저장
chess_board= ["WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW", "BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB"]

# 보드 입력
board = [input().rstrip() for _ in range(N)]

# 다시 칠해야 하는 정사각형 개수 저장
check=[]

# 체스판 선택
for i in range(0, N-7):
  for j in range(M-7):
    str=""
    for k in range(i, i+8):
      str += board[k][j:j+8] 
  
    c_1, c_2 = 0, 0
    # print(str)
    # print(len(str))
    for c in range(64):
      # print(c, str[c], chess_board[0][c], chess_board[1][c])
      if str[c]!=chess_board[0][c]:
        c_1+=1
      if str[c]!=chess_board[1][c]:
        c_2+=1
    check.append(min(c_1, c_2))

print(min(check))