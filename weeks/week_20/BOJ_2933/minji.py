from collections import deque
import sys

input=sys.stdin.readline
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

r, c=map(int, input().split())
arr=[list(input().strip()) for _ in range(r)]
n=int(input())
h=list(map(int, input().split()))
q=deque()

left=1
while n:
    
for i in range(r):
    for j in range(c):
        print(arr[i][j], end='')
    print()