import sys
input = sys.stdin.readline

# 전체 용액의 수 N 입력
N = int(input())

sol = list(map(int, input().split()))
sol.sort()

# 두 포인터 사용
s, e = 0, N-1

# 두 용액의 합, 결과 초기값 설정
sum=sol[0]+sol[N-1]
ans = [sol[s], sol[e]]

# 두 포인터 s<e를 만족하는 동안 반복문
while(s<e):
  # sum과 현재 두 용액의 합 절댓값 비교
  if abs(sol[s]+sol[e])<abs(sum):
    sum=abs(sol[s]+sol[e])
    ans = [sol[s], sol[e]]

  # 뒤 포인터 움직임
  if abs(sol[s]+sol[e]) > abs(sol[s]+sol[e-1]):
    e-=1
  # 앞 포인터 움직임
  else:
    s+=1

print(*ans)