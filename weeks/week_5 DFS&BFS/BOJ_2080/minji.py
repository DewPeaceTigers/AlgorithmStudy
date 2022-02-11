'''
시간초과뜸
'''
import sys

board=[]
for i in range(9) :
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

zero=[]
for i in range(9) : #빈칸의 행, 열 저장
    for j in range(9) :
        if board[i][j]==0 :
            zero.append((i, j))

def check(x, y, a) :
    for i in range(9) :
        if a==board[x][i] : #가로 확인
            return False
        if a ==board[i][y] : #세로 확인
            return False
    #3x3확인
    x=x//3*3
    y=y//3*3
    for i in range(3) :
        for j in range(3) :
            if a == board[i+x][j+y] :
                return False
    return True

def dfs(count) :
    if count==len(zero) :
        for i in range(9) :
            print(*board[i])
        return

    for i in range(1, 10) :
        x=zero[count][0]
        y=zero[count][1]

        if check(x, y, i) :
            board[x][y]=i
            dfs(count+1)
            board[x][y]=0
dfs(0)