import sys
from collections import deque
input=sys.stdin.readline

def bfs() :
    q=deque()
    q.append([home[0], home[1]])
    while q:
        x, y =q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                new_x, new_y = conv[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    q.append([new_x, new_y])
                    visited[i] = 1
    print("sad")
    return

t=int(input())
for _ in range(t) :
    n=int(input())
    home=list(map(int, input().split()))
    conv=[]
    for _ in range(n) :
        x, y=map(int, input().split())
        conv.append([x, y])
    fest=list(map(int, input().split()))
    visited=[0 for i in range(n+1)]
    bfs()
