import sys
input = sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
m=int(input())
search_nums=list(map(int,input().split()))

res={} # 딕셔너리로 하나씩 찾았다.
for num in search_nums:
    res[num]=0
left=0
right=n-1
for num in nums:
    if num in res:
        res[num]+=1

for num in search_nums:
    print(res[num],end=' ')