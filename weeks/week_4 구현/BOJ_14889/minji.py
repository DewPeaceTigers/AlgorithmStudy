'''
1. 팀 구성
함수 중 combination을 이용하여 조합을 구함
서로 다른 n개 중에서 r개를 취하여 조를 만들때 이용
2. 능력치 차이 계산
'''
import itertools

n=int(input())

people=[i for i in range(n)]
S=[[0] for _ in range(n)]

for i in range(n) :
    S[i]=list(map(int, input().split()))

#순열을 이용하여 짝수로 2개의 팀을 나눔
teams=list(itertools.combinations(people, int(n/2)))
min=100*n*n
for team in teams : #두 팀의 능력치 차이 계산
    team_A=0
    team_B=0
    for i in team : #순열로 짝 지은 팀에 포함된 사람들의 능력치 구함
        for j in team:
            team_A+=S[i][j]
    not_team=[x for x in range(n) if x not in team] #순열로 구한 팀에 속하지 않는 사람들
    for i in not_team :
        for j in not_team :
            team_B+=S[i][j]
    
    if min>abs(team_A-team_B) :
        min=abs(team_A-team_B)

print(min)
