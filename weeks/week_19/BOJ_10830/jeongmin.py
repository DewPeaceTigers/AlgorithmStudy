import sys

input = sys.stdin.readline

N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 곱 계산
def mul(NA, A):
  res = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      tmp = 0
      for n in range(N):
        tmp += NA[i][n]*A[n][j]
      res[i][j] = tmp %1000
  return res


# 행렬 A의 B제곱 구하기
def mpow(A, b):
  if b==1:
    # 1000으로 나눈 나머지 저장
    for i in range(N):
      for j in range(N):
        A[i][j] %= 1000

    return A

  else:
    x = mpow(A, b//2) # 분할 
    MA = mul(x, x)  # 행렬 곱 
    if b%2==0:
      return MA
    else:
      return mul(MA, A)

ans = mpow(A, B)

for i in range(N):
  print(*ans[i])