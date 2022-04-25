import sys
input = sys.stdin.readline

n,k = map(int,input().split())
using=list(map(int,input().split()))
taps=[]
cnt=0
for i,u in enumerate(using):
    if u in taps: continue  # 근데 안에 있다면 넘어가기
    if len(taps)!=n:
        taps.append(u)
    else:
        # 가득 찼다면
        rest = using[i:] # 멀티탭 구 수 범위 내에서
        taps_nums=[]
        for j,tap in enumerate(taps):
            if tap in rest:
                taps_nums.append([j,rest.index(tap)])
            else:
                taps_nums.append([j,k+1])
        taps_nums.sort(key=lambda x: (-x[1],x[0])) # 남은 횟수가 작은 순서대로
        taps[taps_nums[0][0]]=u
        cnt+=1
print(cnt)