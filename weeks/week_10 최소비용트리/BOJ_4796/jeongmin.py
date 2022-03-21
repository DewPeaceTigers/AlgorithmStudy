''' [풀이]
강산이가 캠핑장을 사용할 수 있는 최대 일수
1. V%P <L 이면 
  (V//P)*L + V % P
2. V%P >= L 이면
  (V//P)*L + L

2147483645 2147483646 2147483647
776357247 1076006024 2003512866
0 0 0
'''

import sys
input= sys.stdin.readline

ans =[]
while True:
  # (1 < L < P < V)
  L, P, V = map(int, input().split())

  # 마지막 줄인 경우
  if L*P*V ==0:
    break

  # V를 P로 나눈 나머지가 L보다 작은 경우
  if V%P <L: 
    ans.append((V//P)*L + V % P)
  # V를 P로 나눈 나머지가 L보다 큰 경우
  else:
    ans.append((V//P)*L + L)

for i in range(len(ans)):
  print("Case {}: {}".format(i+1, ans[i]))