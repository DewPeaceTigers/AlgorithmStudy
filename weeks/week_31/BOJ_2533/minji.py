import sys

input=sys.stdin.readline

n=int(input())
graph=[[0]*(n+1) for _ in range(n+1)]
for _ in range(n-1) :
    a, b=map(int, input().split())
    graph[a][b]=1

