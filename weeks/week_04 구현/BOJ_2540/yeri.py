# 2580이 맞는 문제
# 못품
import sys
input = sys.stdin.readline
boards=[list(map(int,input().split())) for _ in range(9)]
set_nums = set([n for n in range(10)])
def checkRow(i):
    return list(set_nums-set(boards[i]))
def checkCol(j):
    return list(set_nums-set([boards[c][j] for c in range(9)]))
def checkSquare(i,j):
    dx=[-1,-1,-1,0,0,+1,+1,+1]
    dy=[-1,0,+1,-1,+1,-1,0,+1]
    return list(set_nums-set([ boards[i+dx[t]][j+dy[t]] for t in range(8)]))

for i in range(9):
    for j in range(9):
        if boards[i][j]==0:
            row_left = checkRow(i)
            if len(row_left)==1:
                boards[i][j]=row_left[0]
                continue
            col_left=checkCol(j)
            if len(col_left)==1:
                boards[i][j]=col_left[0]
                continue
            square_left=col_left[:]
            if 0<i<8 and 0<j<8:
                square_left=checkSquare(i,j)
                if len(square_left)==1:
                    boards[i][j]=square_left[0]
                    continue
            boards[i][j]=list(set(row_left)&set(col_left)&set(square_left))[0]
for board in boards:
    for b in board:
        print(b,end=" ")
    print()