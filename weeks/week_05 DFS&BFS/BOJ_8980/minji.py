import sys

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

infos=[[0 for _ in range(N+1)] for _ in range(M+1)]
for i in range(M) :
    start, arrive, box=map(int, sys.stdin.readline().split())
    infos[start][arrive]=box

infos.sort(key=lambda x:x[1]) #받는 마을 번호 기준으로 정렬

delivery=[0 for _ in range(N+1)]
answer=0


for i in range(1, N+1) :
    answer+=delivery[i] #현재 마을에 배달한 박스 수
    rest = C  # 실을 수 있는 수
    for j in range(i+1, N+1) :
        if rest>0:
            if delivery[j] > rest: #j마을에 배달 될 물건이 남은 공간보다 많은 경우
                delivery[j]=rest #남은 공간 만큼만 배달
            rest-=delivery[j]

            if infos[i][j] > rest : #배달할 물건의 수가 남은 공간 보다 큰 경우
                delivery[j]+=rest
                rest=0
            else:
                delivery[j]+=infos[i][j]
                rest-=infos[i][j]
        else: #남은 공간 없는 경우
            delivery[j]=0

print(answer)
