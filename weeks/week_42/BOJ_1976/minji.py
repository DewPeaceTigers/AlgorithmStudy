import sys

input=sys.stdin.readline

n=int(input())
m=int(input())
parents=[i for i in range(n)]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

for i in range(n):
    maps=list(map(int, input().split()))
    for j in range(n) :
        if maps[j]==1:
            union(i, j)

plans=list(map(int, input().split()))

start = parents[plans[0]-1]
ans="YES"
for i in range(1,m):
    if parents[plans[i]-1] != start:
        ans = "NO"
        break

print(ans)