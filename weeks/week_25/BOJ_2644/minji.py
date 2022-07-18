n=int(input())

x, y=map(int, input().split())

m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m) :
    u, v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visit=[0]*(n+1)

def dfs(node) :
    for n in graph[node] :
        if visit[n]==0 :
            visit[n]=visit[node]+1
            dfs(n)
            

dfs(x)

if visit[y]>0 :
    print(visit[y])
else:
    print(-1)