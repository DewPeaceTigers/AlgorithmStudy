# import sys
# input = sys.stdin.readline
# #boards=[list(map(int,input().split())) for _ in range(9)]
# boards=[]
# zero_cnt=0
# for i in range(9):
#     boards.append(list(map(int,input().split())))
#     zero_cnt+=boards[i].count(0)
# set_nums = set([n for n in range(10)])
# def checkRow(i):
#     return list(set_nums-set(boards[i]))
# def checkCol(j):
#     return list(set_nums-set([boards[c][j] for c in range(9)]))
# def checkSquare(i,j):
#     dx=[-1,-1,-1,0,0,+1,+1,+1]
#     dy=[-1,0,+1,-1,+1,-1,0,+1]
#     return list(set_nums-set([ boards[i+dx[t]][j+dy[t]] for t in range(8)]))

# def dfs(x,y):
#     global fill_cnt
#     print(fill_cnt,x,y)
#     if fill_cnt==zero_cnt:
#         for board in boards:
#             for b in board:
#                 print(b,end=" ")
#             print()
#         return
#     else:
#         r=checkRow(x)
#         c=checkCol(y)
#         s=c[:]
#         if 0<x<8 and 0<y<8:
#             s=checkSquare(x,y)
#         candidates=list(set(r)&set(c)&set(s))

#         for candidate in candidates:
#             boards[x][y]=candidate
#             fill_cnt+=1
#             for i in range(x+1,9):
#                 if boards[i][y]==0:
#                     dfs(i,y)
#             for j in range(y+1,9):
#                 if boards[x][j]==0:
#                     dfs(x,j)
#             fill_cnt-=1
#             boards[x][y]=0

# fill_cnt=0
# for i in range(9):
#     for j in range(9):
#         if boards[i][j]==0:
#             dfs(i,j)

import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)