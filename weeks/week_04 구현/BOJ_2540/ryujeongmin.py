import sys
input=sys.stdin.readline

arr=[list(map(int,input().split())) for _ in range(9)]
blank=[]

for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            blank.append((i,j))
  
def checkRow(x,a):
    for i in range(9):
        if a == arr[x][i]:
            return False
    return True 
def checkCol(y,a):
    for i in range(9):
        if a == arr[i][y]:
            return False
    return True

def checkRect(x,y,a):
    x = x//3*3
    y = y//3*3
    for i in range(3):
        for j in range(3):
            if a == arr[x+i][y+j]:
                return False
    return True
    
           
def dfs(n): 
    if n==len(blank):
        for i in range(9):
            print(*arr[i])
        exit(0)
    
	    for i in range(1,10): #blank에 1부터 10까지 모두 넣어봄
        x=blank[n][0]
        y=blank[n][1]
        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i):
            arr[x][y] = i
            dfs(n+1)
            arr[x][y]=0 #다시 0으로 만들어줘야 다른 경우의 수 찾을 수 있음
          
dfs(0)

### ============= 내 틀린 코드 ============= ### 

# import sys
# input=sys.stdin.readline

# sudoku = [list(map(int, input().split())) for _ in range(9)]

# # 빈칸 위치 (행, 열) 저장
# blank=[]
# for i in range(9):
#   for j in range(9):
#     if sudoku[i][j]==0:
#       blank.append([i, j])

# # 정답 한 개만 출력
# findAns=False

# # 게임 규칙 만족하는지 체크
# def check(x, num):
#   r, c = blank[x]
 
#   idx_r, idx_c = (r//3)*3, (c//3)*3

#   # 가로줄 검사
#   for i in range(9):
#     if num==sudoku[r][i]:
#       return False

#   # 세로줄 검사
#   for i in range(9):
#     if num==sudoku[i][c]:
#       return False
  
#   # 정사각형 검사
#   for i in range(3):
#     for j in range(3):
#       if num==sudoku[idx_r+i][idx_c+i]:
#         return False

#   return True

# # 백트래킹
# def bt(x):
#   global findAns 
#   if findAns:
#     return

#   # 빈 칸을 다 채웠다면
#   if x==len(blank):
#     for s in sudoku:
#       print(*s)
#     findAns=True
#     return

#   r, c = blank[x]

#   for i in range(1, 10):
#     # 게임 규칙 만족한다면
#     if check(x, i):
#       sudoku[r][c]=i
#       bt(x+1)
#       sudoku[r][c]=0

# bt(0)