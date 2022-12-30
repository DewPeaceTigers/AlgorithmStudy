import sys, heapq

input=sys.stdin.readline
INF=sys.maxsize

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
count=0
while True :
    count+=1
    n=int(input())
    if n==0 : break
    maps=[list(map(int, input().split())) for _ in range(n)]
    distance=[[INF]*n for _ in range(n)]
    q=[]
    heapq.heappush(q, [maps[0][0], 0, 0])
    distance[0][0]=0
    while q:
        cost, x, y=heapq.heappop(q)
        if x==n-1 and y==n-1 :
            print("Problem {0}: {1}".format(count, distance[n-1][n-1]))
        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n :
                new_cost=cost+maps[nx][ny]
                if new_cost<distance[nx][ny] :
                    distance[nx][ny]=new_cost
                    heapq.heappush(q, [new_cost, nx, ny])