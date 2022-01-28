'''
보드의 최대 가로 세로 길이가 50이므로
하나하나 잘라서 비교해도 오래 걸리지 않기 때문에
보드를 8x8로 자른 후 칠해야하는 수를 파악 후 비교한다.
첫 체스판의 색이 W인 경우와 B인 경우를 나눠서 파악한다.

'''
import sys

n, m=map(int, sys.stdin.readline().split())
board=[[0] for _ in range(n)]
for i in range(n):
    board[i]=list(sys.stdin.readline().rstrip())

min=64

for i in range(n-7) : #8x8만큼 잘라서 비교할거기 때문에 n-8 인덱스까지만 비교하면 됨
    for j in range(m-7) :
        #처음 시작하는 체스판의 색에 따라 다르게 계산해야한다
        paint_W=0
        paint_B=0
        for x in range(i, i+8) : #8x8만큼 잘라서 확인
            for y in range(j, j+8) :
                if (x % 2 ==0 and y % 2 ==0) or (x%2==1 and y%2==1) : 
                #동일한 색이 칠해져야하는 체스판(0번째 행은 짝수 열이 같은 색 1번째 행은 홀수 열이 같은 색 이 점이 반복)
                    if board[x][y]!='W': #첫시작이 W인경우
                        paint_W+=1
                    if board[x][y]!='B':#첫시작이 B인경우
                        paint_B+=1
                else :
                    if board[x][y]!='W': #첫시작이 B인경우
                        paint_B+=1
                    if board[x][y]!='B': #첫시작이 W인경우
                        paint_W+=1
        if min>paint_W :
            min=paint_W
        if min>paint_B :
            min=paint_B
print(min)
                    


