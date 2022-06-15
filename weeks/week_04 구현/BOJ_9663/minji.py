'''
n-queen : 퀸을 하나씩 놓는 자리
check : 퀸을 놓을 수 있는지 확인하는 함수
퀸은 상하좌우, 대각선 아무곳이나 다 이동할 수 있으므로
각 행마다 하나씩 놓여져야한다
1일땐 퀸이 있는 경우 0 이면 퀸이 없는 경우
=>시간초과 발생
'''
def check(x, y): #퀸을 놓아도 되는지 파악
    for i in range(x) :
        for j in range(n) :
            if j==y and i!=x and board[i][j]==1 : #수직인 위치 판별
                return False
            elif abs(i-x)==abs(j-y) and board[i][j]==1: #대각선 판별
                return False
    return True

def queen(x) :
    global ans, board
    if x==n : #퀸이 n개 놓여져있으면 종료
        ans+=1
        return
    for i in range(n) :
        board[x][i]=1
        if check(x, i) :
            queen(x+1)
            board[x][i]=0
        else:
            board[x][i]=0

n=int(input())
ans=0
board=[[0]*n for _ in range(n)]

for i in range(n) :
    board[0][i]=1
    queen(1)
    board[0][i]=0
print(ans)