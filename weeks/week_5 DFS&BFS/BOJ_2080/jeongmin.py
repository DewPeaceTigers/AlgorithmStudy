import sys
input=sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]

# 빈칸 위치 (행, 열) 저장
blank=[]
for i in range(9):
  for j in range(9):
    if sudoku[i][j]==0:
      blank.append([i, j])

# 정답 한 개만 출력
findAns=False

# 게임 규칙 만족하는지 체크
def check(x, num):
  r, c = blank[x]
 
  idx_r, idx_c = (r//3)*3, (c//3)*3

  # 가로줄 검사
  for i in range(9):
    if num==sudoku[r][i]:
      return False

  # 세로줄 검사
  for i in range(9):
    if num==sudoku[i][c]:
      return False
  
  # 정사각형 검사
  for i in range(3):
    for j in range(3):
      if num==sudoku[idx_r+i][idx_c+j]:
        return False

  return True

# 백트래킹
def bt(x):
  global findAns 
  if findAns:
    return

  # 빈 칸을 다 채웠다면
  if x==len(blank):
    for s in sudoku:
      print(*s)
    findAns=True
    return

  r, c = blank[x]

  for i in range(1, 10):
    # 게임 규칙 만족한다면
    if check(x, i):
      sudoku[r][c]=i
      bt(x+1)
      sudoku[r][c]=0

bt(0)