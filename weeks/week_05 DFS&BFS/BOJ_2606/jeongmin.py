'''[풀이]
dfs 사용, 인접리스트 방식
'''

import sys
input = sys.stdin.readline

# 컴퓨터의 수 입력
N = int(input())

# 컴퓨터 쌍의 수 입력
T = int(input())

# 컴퓨터 연결 정보 저장
com = [[] for _ in range(N+1)]
for _ in range(T):
  a, b = map(int, input().split())
  com[a].append(b)
  com[b].append(a)

# 바이러스 감염 여부 저장
virus = [False]* (N+1)

# 1번 바이러스
virus[1] = True

# 웜 바이러스에 걸리게 되는 컴퓨터의 수
cnt = 0

def dfs(i):
  global cnt
  for x in com[i]:
    if not virus[x]:
      # 해당 컴퓨터 감염
      cnt+=1
      virus[x]= True
      dfs(x)

dfs(1)

print(cnt)