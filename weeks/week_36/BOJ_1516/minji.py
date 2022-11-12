'''
https://m.blog.naver.com/ndb796/221236874984
'''
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
building=[[] for _ in range(n+1)]
degree=[0]*(n+1) #진입차수
cost=[0]*(n+1)
answer=[0]*(n+1)
q=deque()
for i in range(1, n+1) :
    data=list(map(int, input().split()))
    cost[i]=data[0]
    for data in data[1:-1] :
        building[data].append(i)
        degree[i]+=1

for i in range(1, n+1):
    if degree[i]==0:
        q.append(i)
        answer[i]=cost[i]

while q :
    x=q.popleft()
    for i in building[x] :
        degree[i]-=1
        answer[i]=max(answer[i], answer[x]+cost[i])
        if degree[i]==0:
            q.append(i)
for i in range(1, n+1):
    print(answer[i])