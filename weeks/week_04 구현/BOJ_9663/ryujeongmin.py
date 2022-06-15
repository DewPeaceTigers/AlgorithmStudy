import sys
input = sys.stdin.readline

# N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
N = int(input())

col= [0]*N
ans=0

# 가능한지 체크
def check(x):
  for i in range(x):
    if col[x]==col[i] or abs(col[x]-col[i])==x-i:
      return False
  return True

def bt(x):
  global ans

  # 가능한 경우
  if x==N:
    ans+=1
    return

  for i in range(N):
    col[x]=i
    if check(x):
      bt(x+1)
      
bt(0)
print(ans)