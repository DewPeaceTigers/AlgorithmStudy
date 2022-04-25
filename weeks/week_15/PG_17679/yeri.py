from collections import deque
def find(board,n,m):
    pop=set()
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]!=0:
                pop |= set([(i,j),(i,j+1),(i+1,j),(i+1,j+1)])
    for i,j in pop:
        board[i][j]=0
    return len(pop)
def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i]=list(board[i])
    cnt=0
    idx=0
    while True:
        this_cnt=find(board,n,m)
        if this_cnt==0: break # 더이상 터뜨릴 거 없음
        cnt+=this_cnt
        for j in range(n):
            cur=[ board[i][j] for i in range(m)]
            empty=[0]*cur.count(0)
            cur = empty+[ c for c in cur if c!=0]
            for i,c in enumerate(cur):
                board[i][j]=c
    return cnt
