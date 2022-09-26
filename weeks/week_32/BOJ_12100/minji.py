import sys, copy

n=int(sys.stdin.readline())

boards=[]

def move(dir) :
    if dir==0: #위로 이동
        for i in range(n) :
            index=0
            for j in range(1, n) :
                if boards[j][i] :
                    temp=boards[j][i]
                    boards[j][i]=0
                    if boards[index][i] == 0 :
                        boards[index][i]=temp
                    elif boards[index][i]==temp :
                        boards[index][i]=temp*2
                        index+=1
                    else:
                        index+=1
                        boards[index][i]=temp

    elif dir==1: #아래로 이동
        for i in range(n) :
            index=n-1
            for j in range(n-2, -1, -1) :
                if boards[j][i] :
                    temp=boards[j][i]
                    boards[j][i]=0
                    if boards[index][i]==0 :
                        boards[index][i]=temp
                    elif boards[index][i]==temp :
                        boards[index][i]=temp*2
                        index-=1
                    else:
                        index-=1
                        boards[index][i]=temp

    elif dir==2: #좌로 이동
        for i in range(n):
            index = 0
            for j in range(1, n):
                if boards[i][j]:
                    temp = boards[i][j]
                    boards[i][j] = 0
                    if boards[i][index] == 0:
                        boards[i][index] = temp
                    elif boards[i][index] == temp:
                        boards[i][index] = temp * 2
                        index += 1
                    else:
                        index += 1
                        boards[i][index] = temp
    else : #우로 이동
        for i in range(n) :
            index=n-1
            for j in range(n-2, -1, -1) :
                if boards[i][j] :
                    temp=boards[i][j]
                    boards[i][j]=0
                    if boards[i][index]==0:
                        boards[i][index]=temp
                    elif boards[i][index]==temp :
                        boards[i][index]=temp*2
                        index-=1
                    else:
                        index-=1
                        boards[i][index]=temp

def dfs(count) :
    global ans, boards
    if count==5 :
        for i in range(n) :
                ans=max(ans, max(boards[i]))
        return

    temp=copy.deepcopy(boards)
    for i in range(4) :
        move(i) #0~3일때 상하좌우 이동
        dfs(count+1)
        boards=copy.deepcopy(temp)

for i in range(n) :
    boards.append(list(map(int, sys.stdin.readline().split())))

ans=0
dfs(0)
print(ans)