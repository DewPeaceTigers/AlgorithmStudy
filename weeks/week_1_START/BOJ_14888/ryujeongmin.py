''' [풀이]
못 풀었던 문제..

백트래킹을 이용
    - 연산자가 존재하면 그 연산을 수행하며 재귀 호출을 통해 탐색 진행 

'''

# N 입력 (2 ≤ N ≤ 11)
N = int(input())

# A1, A2, ..., AN ((1 ≤ Ai ≤ 100)) 입력
A = list(map(int, input().split()))

# 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)의 개수 입력
plus, sub, multi, divide = map(int, input().split())

r_max, r_min = int(-1e9), int(1e9)

def result(i, r, p, s, m, d):
  global r_max, r_min
  if i==N-1:
    r_max, r_min = max(r_max, r), min(r_min, r)
  else:
    if p: result(i+1, r+A[i+1], p-1, s, m, d)
    if s: result(i+1, r-A[i+1], p, s-1, m, d)
    if m: result(i+1, r*A[i+1], p, s, m-1, d)
    if d: result(i+1, int(r/A[i+1]), p, s, m, d-1)

result(0, A[0], plus, sub, multi, divide)

print(r_max)
print(r_min)
