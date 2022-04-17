import sys
input= sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

# 덧셈, 뺄셈, 곱셈, 나눗셈 개수 입력
p, s, m, d = map(int, input().split())

res_max = -1e9 
res_min = 1e9 

def dfs(i, p, s, m, d, A, sum):
  global res_max
  global res_min
  if p==0 and s==0 and m==0 and d==0:
    # print(sum)
    res_max = max(res_max, sum)
    res_min = min(res_min, sum)
  
  if p: # 덧셈
    dfs(i+1, p-1, s, m, d, A, sum+A[i+1])
  if s: # 뺄셈
    dfs(i+1, p, s-1, m, d, A, sum-A[i+1])
  if m: # 곱셈
    dfs(i+1, p, s, m-1, d, A, sum*A[i+1])
  if d: # 나눗셈
    # '음수 나누기 양수' 인 경우 고려
    y = sum//A[i+1] if sum>0 else -((-sum)//A[i+1])
    dfs(i+1, p, s, m, d-1, A, y)


dfs(0, p, s, m, d, A, A[0])

print(res_max)
print(res_min)