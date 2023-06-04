import sys

input=sys.stdin.readline

n=int(input())
start=list(map(int, input().rstrip()))
final=list(map(int, input().rstrip()))

def check(start, final) :
    if start==final :
        return 0
    cnt = 0
    tmp = start[:]

    for i in range(1, n) :
        if tmp[i-1]==final[i-1] :
            continue
        cnt+=1
        for j in range(i-1, i+2) :
            if j<n:
                tmp[j]=1-tmp[j]
    return cnt if tmp==final else float('inf')
#첫번째 스위치를 안 누른 경우
result=check(start, final)

#첫번째 스위치 누른 경우
start[0]=1-start[0]
start[1]=1-start[1]
ans=min(result, check(start, final)+1)
print(ans if ans!=float('inf') else -1)