n=int(input())
v=int(input())
graph=[]

for i in range(v) :
    graph.append(list(map(int, input().split())))

visit=[0]*(n+1)

def dfs(x) :
    visit[x]=1 #이미 확인 했었는지 파악
    for i in range(v) :
        if graph[i][0] == x and visit[graph[i][1]]==0 : #연결되어있는지 확인 + 방문한적 없는지 
            dfs(graph[i][1])
        if graph[i][1] == x and visit[graph[i][0]]==0 :
            dfs(graph[i][0])
dfs(1)
print(sum(visit)-1)
