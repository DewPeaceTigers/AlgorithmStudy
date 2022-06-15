import sys
input = sys.stdin.readline

K,N=map(int,input().split())

lines=[int(input()) for _ in range(K)]

start,end=1,max(lines)
while start <= end:
    mid = (start+end)//2

    cnt=0
    for i in range(K):
        cnt+=lines[i]//mid

    if cnt >= N: # 더 많거나 같으면 큰 쪽으로 범위 옮기기 (나누기니깐)
        start = mid+1
    else:
        end = mid-1
print(start-1)