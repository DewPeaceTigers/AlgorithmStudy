"""
매개 변수 탐색

"""
import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
trees=list(map(int,input().split()))

start,end=1,max(trees)

while start<=end:
    mid=(start+end)//2

    cut=0
    for tree in trees:
        cut+=(tree-mid if tree-mid>=0 else 0)

    if cut >= m:
        start=mid+1
    else:
        end=mid-1
print(start-1)
