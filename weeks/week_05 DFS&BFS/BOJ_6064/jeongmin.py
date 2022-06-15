'''[풀이]
x값을 고정시킨 뒤 y값을 찾아보기
ex) M=10, x=3인 경우 -> 3, 13, 23, 33, ....
'''

import sys
input = sys.stdin.readline

# T 입력
T = int(input())

for _ in range(T):
  # M, N, x, y 입력
  M, N, x, y = map(int, input().split())

  ans=-1
  for i in range(N):
    # x가 나올 수 있는 수 차례로 확인
    n = M*i+x

    # <x:y> 가 나오는 경우
    if n%M==x%M and n%N==y%N:
      ans=n
      break
  
  print(ans)