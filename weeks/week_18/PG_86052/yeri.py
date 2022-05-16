def findCycle(dir,x,y,visits,grids):
    dirs={
        'S':[0,1,2,3],
        'L':[1,2,3,0],
        'R':[3,0,1,2]
    }
    dx = [+1, 0, -1, 0]
    dy = [0, +1, 0, -1]
    if visits[x][y][dir]: return 0
    visits[x][y][dir]= True
    i,j,d = x,y,dir
    time=0 
    while True:
        time+=1
        nx = (i+dx[d])%len(grids)
        ny = (j+dy[d])%len(grids[0])
        d = dirs[grids[nx][ny]][d]
        if nx==x and ny==y and d==dir : break
        i,j=nx,ny
        visits[i][j][d]=True
    return time

def solution(grids):
    for i in range(len(grids)):
        grids[i]=list(grids[i])
    visits=[ [[False]*4 for j in range(len(grids[i]))] for i in range(len(grids)) ]
    pathes=[]
    for i in range(len(grids)):
        for j in range(len(grids[i])):
            for d in range(4):
                temp = findCycle(d,i,j,visits,grids)
                if temp!=0 : pathes.append(temp)
    pathes.sort()
    return pathes