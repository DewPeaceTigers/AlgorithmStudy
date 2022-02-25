import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    idx=0
    cnt=0
    for i in range(n):
        while idx<m:
            if b[idx]>=a[i]:
                break
            idx+=1
        cnt+=idx
    print(cnt)