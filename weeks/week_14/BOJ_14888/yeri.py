import sys

input = sys.stdin.readline

n = int(input())
A=list(map(int,input().split()))
op=list(map(int,input().split()))
min_sum,max_sum=int(1e9),int(-1e9)
def make(idx,sum,p,m,g,d):
    global min_sum,max_sum
    if idx == n:
        min_sum=min(min_sum,sum)
        max_sum=max(max_sum,sum)
        return
    if p!=0: make(idx+1,sum+A[idx],p-1,m,g,d)
    if m!=0: make(idx+1,sum-A[idx],p,m-1,g,d)
    if g!=0: make(idx+1,sum*A[idx],p,m,g-1,d)
    if d!=0: make(idx+1,int(sum/A[idx]),p,m,g,d-1)

make(1,A[0],op[0],op[1],op[2],op[3])
print(max_sum)
print(min_sum)