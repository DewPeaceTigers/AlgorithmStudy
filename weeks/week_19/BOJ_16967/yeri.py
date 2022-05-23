import sys
input = sys.stdin.readline

H,W,X,Y = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(H+X)]

A = [[0]*W for _ in range(H)]
check = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i+X<H and j+Y<W : check[i+X][j+Y]+=1

for i in range(H):
    for j in range(W):
        if check[i][j]==0:
            A[i][j]=B[i][j]
        else:
            A[i][j]=B[i][j]-A[i-X][j-Y]
for a in A: print(*a)