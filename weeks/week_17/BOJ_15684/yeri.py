import sys
input = sys.stdin.readline

# 브루트포스로 가로선을 놓을 수 있는 곳에 놓을 수 있는지 확인하고 매번 출발점에서 도착점으로 가는지 확인하기

n,m,h = map(int,input().split())
spaces=[[False]*n for _ in range(h)]
if m==0:
    print(0)
    exit(0)
for _ in range(m):
    a,b = map(int,input().split())
    spaces[a-1][b-1]=True


def check():
    for i in range(n):
        cur_y = i
        for j in range(h):
            if spaces[j][cur_y]: cur_y+=1 # 우측 존재 이동
            elif cur_y > 0 and spaces[j][cur_y-1]: cur_y-=1 # 좌측 존재 이동
        if cur_y != i : return False
    return True
    # for i in range(n):
    #     cur_x,cur_y = 0,i
    #     while cur_x!=h-1: # 맨 아래에 도착했을 때
    #         print(i,cur_x,cur_y)
    #         if spaces[cur_x][cur_y+1]:
    #             cur_y+=1 # 오른쪽으로 이동
    #         elif -1<cur_y-1<n and spaces[cur_x][cur_y-1]:
    #             cur_y-=1 # 왼쪽으로 이동
    #         cur_x+=1 # 아래로 한 칸 이동때
    #     if cur_y != i : return False
    # return True
def dfs(cnt,x,y):
    global min_cnt
    if check():
        min_cnt = min(min_cnt,cnt)
        print('---')
        return
    elif cnt == 3 or min_cnt <= cnt: return
    for i in range(x,h):
        if i == x : k = y # 행이 변경되기 전까지 가로선을 계속해서 탐색. 이전에 했던 것은 탐색하지 않기 위함
        else : k = 0 # 행이 변경되면 가로선 처음부터 탐색
        for j in range(k,n-1): # 세로선 탐색
            if not spaces[i][j] and not spaces[i][j+1]: # 오른쪽 없을 경우
                if j > 0 and spaces[i][j-1]: continue # 왼쪽 존재할 경우
                spaces[i][j]=True
                dfs(cnt+1,i,j+2) # 가로선 2칸 이동
                spaces[i][j]=False # 백트래킹

min_cnt=4
dfs(0,0,0)
print(min_cnt if min_cnt<4 else -1)

