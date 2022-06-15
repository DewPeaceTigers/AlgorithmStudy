'''
높이를 기준으로 이진탐색을 하는데
높이를 설정하고 나무를 잘랐을 때 총 합을 M과 비교
'''
import sys

N, M=map(int, input().split())
tree=list(map(int, sys.stdin.readline().split()))
start, end=1, max(tree)
answer=0
while start<=end:
    mid=(start+end)//2

    sum=0
    for i in tree:
        if i >mid:
            sum+=i-mid
            if sum==M :
                break
    if sum>=M:
        start=mid+1
    else:
        end=mid-1

print(end)
