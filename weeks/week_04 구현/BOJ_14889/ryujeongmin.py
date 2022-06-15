from itertools import combinations
import sys
input = sys.stdin.readline

# N(4 ≤ N ≤ 20, N은 짝수) 입력
N = int(input())
n = [i for i in range(N)]

# 능력치 S 입력
S = [list(map(int, input().split())) for _ in range(N)]

# 조합 리스트 저장
comb = list(combinations(n, N//2))

# 조합 리스트 크기 저장
l = len(comb)

ans=-1

for i in range(l//2):
  start=0 # 스타트 팀 능력치
  link=0 # 링크 팀 능력치

  # print("모든 조합 확인", comb[i], comb[l-1-i])
  for j in range(N//2-1):
    for k in range(j+1, N//2):
      # print(comb[i][j], comb[i][k]) # 스타트 팀
      start+= S[comb[i][j]][comb[i][k]]+S[comb[i][k]][comb[i][j]]
      # print(comb[l-1-i][j], comb[l-1-i][k]) # 링크 팀
      link += S[comb[l-1-i][j]][comb[l-1-i][k]]+S[comb[l-1-i][k]][comb[l-1-i][j]]
  # print(start, link)

  # 처음 나온 결과 ans에 대입
  if ans ==-1:
    ans = abs(start-link)
  # 최솟값 비교하여 넣기
  else:
    ans = min(ans, abs(start-link))

# 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소
print(ans)