import sys
input = sys.stdin.readline
c=int(input())
n=int(input())
edge={}
for i in range(1,c+1):
    edge[i]=[]
for _ in range(n):
    i,j=map(int,input().split())
    edge[i].append(j)
    edge[j].append(i)
def dfs(need=[1],visit=[1]):
    cnt=-1
    while need:
        now=need.pop(0)
        cnt+=1
        for e in edge[now]:
            if e not in visit:
                need.append(e)
                visit.append(e)
    return cnt
#cnt=0

print(dfs())