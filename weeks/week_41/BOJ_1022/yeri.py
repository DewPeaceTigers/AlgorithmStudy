import sys
input = sys.stdin.readline

r1,c1,r2,c2 = map(int,input().split())

n = max(abs(r1),abs(r2))
m = max(abs(c1),abs(c2))
real_n = abs(r1-r2)+1
real_m = abs(c1-c2)+1


l = max(n,m)

ur = r1+l
uc = c1+l
vr = r2+l
vc = c2+l
r = c = l
board = [[0]*real_m for _ in range(real_n)]

add = 1
level = 1
d = 0
dr = [0,-1,0,+1]
dc = [+1,0,-1,0]

while add <= (l*2+1)**2:
    if ur<=r<=vr and uc<=c<=vc: board[r-ur][c-uc] = add
    add+=1
    nr=r+dr[d]
    nc=c+dc[d]
    if not(l-level <= nr <= l+level) or not(l-level<= nc<=l+level):
        d+=1
        if d==4:
            level+=1
            d=0
    r += dr[d]
    c += dc[d]
m = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        m = max(m,board[i][j])
mstr = str(m)
length = len(mstr)

for i in range(real_n):
    for j in range(real_m):
        tmp = str(board[i][j])
        print(tmp.rjust(length," "), end = ' ')
    print()