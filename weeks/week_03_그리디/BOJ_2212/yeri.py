import sys
input=sys.stdin.readline

N=int(input())
K=int(input())
sensors=list(map(int,input().split()))
if K>=N: # 집중국 개수가 센서 개수보다 많으면 수신가능영역 0, 이걸 안하면 런타임에러 뜬다.
    print(0)
    sys.exit()
    
sensors.sort()
distance=[(i,sensors[i+1]-sensors[i]) for i in range(len(sensors)-1)] # 어느 구간인지 명시하기 위해 i를 저장함
distance.sort(key=lambda x:x[1],reverse=True)

pre_i=0
answer=0
for i in range(K-1):
    answer+= sensors[distance[i][0]] - sensors[pre_i] # 구간 사이 거리 계산
    pre_i=distance[i][0]+1
answer+=sensors[len(sensors)-1] - sensors[pre_i]
print(answer)