import sys
input = sys.stdin.readline

N = int(input())
board = [ list(map(int,input().split())) for _ in range(N)]

max_num=0
def game(cnt):
    global max_num
    if cnt==5:
        for i in range(N):
            max_num = max(board[i]+[max_num])
        return

    temp = []
    for i in range(N):
        # 초기화 용도
        temp.append(board[i][:])

    # # 위 쪽
    for j in range(N):
        col = [ board[i][j] for i in range(N)]
        # print(col)
        newCol = [0]*N
        idx=0
        for i in range(N):
            if col[i]!=0:
                if idx==0 or newCol[idx-1]!=col[i]:
                    newCol[idx]=col[i]
                    idx+=1
                else:
                    newCol[idx-1]*=2
        # board 세팅
        for i in range(N):
            board[i][j]=newCol[i]
    game(cnt+1)
    for i in range(N):
        board[i]=temp[i]

    # 아래 쪽
    for j in range(N):
        col = [ board[i][j] for i in range(N)]
        newCol = [0]*N
        idx=N-1
        for i in range(N-1,-1,-1):
            if col[i]!=0:
                if idx==N-1 or newCol[idx+1]!=col[i]:
                    newCol[idx]=col[i]
                    idx-=1
                else:
                    newCol[idx+1]*=2
        for i in range(N):
            board[i][j]=newCol[i]
    game(cnt+1)
    for i in range(N):
        board[i]=temp[i]

    # 왼 쪽
    for i in range(N):
        row = [board[i][j] for j in range(N)]
        newRow = [0] * N
        idx = 0
        for j in range(N):
            if row[j] != 0:
                if idx==0 or newRow[idx-1]!=row[j]:
                    newRow[idx] = row[j]
                    idx += 1
                else:
                    newRow[idx-1]*=2

        for j in range(N):
            board[i][j]=newRow[j]
    game(cnt+1)
    for i in range(N):
        board[i]=temp[i]

    # 오른 쪽
    for i in range(N):
        row = [board[i][j] for j in range(N)]
        newRow = [0] * N
        idx = N-1
        for j in range(N-1,-1,-1):
            if row[j] != 0 :
                if idx==N-1 or newRow[idx+1]!=row[j]:
                    newRow[idx] = row[j]
                    idx -= 1
                else:
                    newRow[idx+1]*=2
        for j in range(N):
            board[i][j]=newRow[j]
    game(cnt+1)
    for i in range(N):
        board[i]=temp[i]
game(0)
print(max_num)

# 실패