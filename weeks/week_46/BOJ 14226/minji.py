from collections import deque

S=int(input())

visit=[[-1]*(S+1) for _ in range(S+1)]
visit[1][0]=0

q=deque()
q.append([1, 0])

while q :
    now, clip=q.popleft()

    if visit[now][now]==-1 : #과정1
        visit[now][now]=visit[now][clip]+1
        q.append([now, now])

    if now+clip<=S and visit[now+clip][clip]==-1 : #과정2
        visit[now+clip][clip]=visit[now][clip]+1
        q.append([now+clip, clip])

    if now-1>0 and visit[now-1][clip]==-1 : #과정3
        visit[now-1][clip]=visit[now][clip]+1
        q.append([now-1, clip])

ans=float('inf')
for i in range(S+1) :
    if visit[S][i]!=-1 and ans>visit[S][i] :
        ans=visit[S][i]

print(ans)