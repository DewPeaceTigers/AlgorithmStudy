import sys
input = sys.stdin.readline

n = int(input())
space=[[0]*(n+1)]
for _ in range(n):
    space.append([0]+list(map(int,input().split())))
min_diff=int(1e9)
for d1 in range(1,n+1):
    for d2 in range(1,n+1):
        for x in range(1,n+1):
            for y in range(1,n+1):
                if 1<=x<x+d1+d2<=n and 1<=y-d1<y<y+d2<=n:
                    temp = [[0] * (n + 1) for i in range(n + 1)]
                    for i in range(d1 + 1):
                        temp[x + i][y - i] = 5
                        temp[x + d2 + i][y + d2 - i] = 5
                    for i in range(d2 + 1):
                        temp[x + i][y + i] = 5
                        temp[x + d1 + i][y - d1 + i] = 5
                    for i in range(x + 1, x + d1 + d2):
                        isTrue = False
                        for j in range(1, n + 1):
                            if temp[i][j] == 5: isTrue = not isTrue
                            if isTrue: temp[i][j] = 5
                    areas = [0] * 5
                    for i in range(1,n+1):
                        for j in range(1,n+1):
                            if 1<=i<x+d1 and 1<=j<=y and temp[i][j] == 0: areas[0]+=space[i][j]
                            elif 1<=i<=x+d2 and y<j<=n and temp[i][j] == 0: areas[1]+=space[i][j]
                            elif x+d1<=i<=n and 1<=j<y-d1+d2 and temp[i][j] == 0: areas[2]+=space[i][j]
                            elif x+d2<i<=n and y-d1+d2<=j<=n and temp[i][j] == 0: areas[3]+=space[i][j]
                            else: areas[4]+=space[i][j]
                    areas.sort()
                    min_diff = min(min_diff, areas[-1]-areas[0])
print(min_diff)