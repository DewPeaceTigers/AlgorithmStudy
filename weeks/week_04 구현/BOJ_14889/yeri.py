# from itertools import combinations
# N=int(input())
# s=[]
# for i in range(N):
#     s.append(list(map(int,input().split())))
# num_list = {i for i in range(len(s))}
# teams_list=list(combinations(num_list,N//2))
# min_skill=100000
# for team in teams_list:
#     sum_1,sum_2=0,0
#     for t in combinations(team,2):
#         sum_1+=(s[t[0]][t[1]]+s[t[1]][t[0]])
#     for t in combinations(num_list.difference(list(team)),2):
#         sum_2+=(s[t[0]][t[1]]+s[t[1]][t[0]])
#     min_skill=min(abs(sum_1-sum_2),min_skill)
# print(min_skill)

from itertools import combinations
n=int(input())
s=[list(map(int,input().split())) for _ in range(n)]
teams=combinations([i for i in range(n)],n//2)
print(teams)
origin=set([i for i in range(n)])
min_gap=int(1e9)
for team in teams:
    print(team)
    others=list(origin-set(team))
    print(team,others)
    sum_a,sum_b=0,0
    for i in range(n//2):
        for j in range(i+1,n//2):
            sum_a+=s[team[i]][team[j]]+s[team[j]][team[i]]
            sum_b+=s[others[i]][others[j]]+s[others[j]][others[i]]
    min_gap=min(min_gap,abs(sum_a-sum_b))
print(min_gap)

# 백트래킹으로 풀었으나 시간 초과 걸림.. 이유는 모르겟음...
# n=int(input())
# s=[list(map(int,input().split())) for _ in range(n)]
# origin=set([i for i in range(n)])
# def dfs(cnt,team):
#     global min_gap
#     if cnt==n//2:
#         # 팀원을 다 골랐다면
#         other = list(origin-set(team))
#         gap=0
#         for i in range(n//2):
#             for j in range(i+1,n//2):
#                 gap+= (s[team[i]][team[j]]+s[team[j]][team[i]])-(s[other[i]][other[j]]+s[other[j]][other[i]])
#         min_gap=min(min_gap,abs(gap))
#     else:
#         for i in range(n):
#             if i not in team:
#                 team.append(i)
#                 dfs(cnt+1,team)
#                 team.pop()
# min_gap=int(1e9)
# dfs(0,[])
# print(min_gap)

