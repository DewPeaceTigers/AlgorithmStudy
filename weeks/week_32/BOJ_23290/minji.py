'''
틀렸어요..틀렸습니다..
'''
import copy
dx=[-1, 0, 1, 0]
dy=[0, -1, 0, 1]
fish_dx=[-1, 0, 1, 0, -1, 1, -1, 1]
fish_dy=[0, -1, 0, 1, -1, 1, 1, -1]

def move_fish():
    """
    물고기 이동
    1. 상어가 있는 칸, 물고기 냄새 칸, 벗어나는 칸 x
    2. 45도 반시계 회전 후 이동. 이동 못하는 경우 그대로
    :return:
    """
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + fish_dx[i], y + fish_dy[i]
                    if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        res[nx][ny].append(i)
                        break
                else:
                    res[x][y].append(d)
    return res

def dfs(x, y, dep, count, visit):
    global max_eat, shark, eat
    if dep==3:
        if count>max_eat:
            max_eat=count
            shark=[x, y]
            eat=visit[:]
        return

    for i in range(4) :
        nx=x+dx[i]
        ny=y+dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visit:  # 처음 방문, cnt에 죽은 물고기 수 추가
                visit.append((nx, ny))
                dfs(nx, ny, dep + 1, count + len(temp[nx][ny]), visit)
                visit.pop()
            else:  # 방문한 경우
                dfs(nx, ny, dep + 1, count, visit)


m, s = map(int, input().split())
graph = [[[] for _ in range(4)] for _ in range(4)]

for _ in range(m):
    x, y, d=map(int, input().split())
    graph[x - 1][y - 1].append(d - 1)

smell=[[0]*4 for _ in range(4)] #물고기 냄새
shark=list(map(int, input().split())) #상어 위치
shark[0]-=1
shark[0]-=1

for _ in range(s) :
    eat = list()
    max_eat=0
    temp=copy.deepcopy(graph) #1.물고기 복제
    temp=move_fish() #2.물고기 이동
    dfs(shark[0], shark[1], 0, 0, list()) #3.상어 이동
    for x, y in eat:
        if temp[x][y] :
            temp[x][y]=[]
            smell[x][y]=3

    #4. 냄새 사라짐
    for i in range(4) :
        for j in range(4) :
            if smell[i][j] :
                smell[i][j]-=1

    #5. 복제 마법
    for i in range(4) :
        for j in range(4) :
            graph[i][j]+=temp[i][j]
# 물고기 수 구하기
    answer = 0
    for i in range(4):
        for j in range(4):
            answer += len(graph[i][j])

    print(answer)