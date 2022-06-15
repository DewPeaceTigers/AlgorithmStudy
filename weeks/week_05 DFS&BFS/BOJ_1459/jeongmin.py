'''[풀이]
대각선 두번(2*s)으로 갈 수 있는 경우
 - (x+2, y+2) | (x+2, 0) | (0, y+2)
 - 위의 세 경우를 가로나 세로로만 간 경우 각각 걸리는 시간 : 4*w, 2*w, 2*w

s>=2w, w<=s<2w, s<w 이렇게 세가지 경우로 나누어 푼다.
1. s>=2w
  - 가로나 세로로만 가는 것이 최소 시간
2. w<=s<2w
  - 대각선으로 (x+1, y+1) 갈 수 있는 만큼 최대한 가고 : min(x, y)
  - 나머지를 가로나 세로로 움직여 이동함 : abs(x-y)
3. s<w
  - 대각선으로 최대한 많이 이동
  - abs(x-y)가 홀수인 경우는 대각선 이동 횟수 하나 빼고 가로나 세로로 한번 더 이동함
'''

import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())
ans=0

# s >= 2w
if s>= 2*w:
  ans = (x+y)*w

# s >= w
elif s>=w:
  ans = abs(x-y)*w + min(x, y)*s

# s < w
else:
  # n: 대각선으로 이동한 횟수
  n = min(x, y) + abs(x-y)

  if abs(x-y)%2==0:
    ans = n*s

  else:
    # 대각선으로는 (x+2, 0), (0, y+2) 가능
    # abs(x-y)값이 홀수이면 -1 해줘야함
    ans = w+ (n-1)*s

print(ans)