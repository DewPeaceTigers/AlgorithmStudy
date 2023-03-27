import sys

input=sys.stdin.readline

n=int(input())
kinds=list(map(int, input().split()))

start, end=0, n-1

answer=[kinds[start], kinds[end]]
cur=abs(answer[0]+answer[1])
tmp=float('inf')
while start<end :
    tmp=kinds[start]+kinds[end]
    if cur>abs(tmp) :
        answer[0], answer[1]=kinds[start], kinds[end]
        cur=abs(tmp)
    if tmp==0 : break
    if tmp>0 :
        end-=1
    else:
        start+=1

print(*answer)