import sys
from collections import deque
input = sys.stdin.readline

def bfs(cur,dest):
    q = deque([[0,cur]])
    border= max(cur,dest)*2
    visit = [False]*(border*2+1)
    visit[cur]=True
    while q :
        time,c = q.popleft()
        if c == dest : return time
        if 0<=c*2<=border and not visit[c*2]:
            visit[c*2]=True
            q.append([time+1,c*2])
        if 0<=c+1<=border and not visit[c+1]:
            visit[c + 1] = True
            q.append([time+1,c+1])
        if 0<=c-1<=border and not visit[c-1]:
            visit[c - 1] = True
            q.append([time+1,c-1])

N,K = map(int,input().split())

print(bfs(N,K))

'''
단순 bfs 문제
대신 시간 초과,, 잘 해결하기
visit을 append 하는 것보다 t/f 로 해주는 것이 시간이 덜 들어감
'''