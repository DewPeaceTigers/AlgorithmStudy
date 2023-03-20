#풀이참고

from collections import deque
n=int(input())

q=deque()
q.append([1, 0])

visit=[[-1]*(n+1) for _ in range(n+1)]
visit[1][0]=0
while q:
    now, clip=q.popleft()
    if visit[now][now]==-1 :
        visit[now][now]=visit[now][clip]+1
        q.append([now, now])
    if now+clip<=n and visit[now+clip][clip]==-1 :
        visit[now+clip][clip]=visit[now][clip]+1
        q.append([now+clip, clip])
    if now-1>=0 and visit[now-1][clip]==-1 :
        visit[now-1][clip]=visit[now][clip]+1
        q.append([now-1, clip])
ans=-1
for i in range(n+1) :
    if visit[n][i] !=-1 :
        if ans==-1 or visit[n][i]<ans :
            ans=visit[n][i]
print(ans)
