''' [풀이]
1. sys.stdin.readline 이용하여 여러줄 입력 (input()으로 하면 시간초과)
2. 큐 - collections 모듈 deque 사용
3. 조건문으로 각 명령어 확인

[명령 종류]
push X : q.append(x)
pop    : q.popleft()
size   : len(q)
empty  : len(q)==0
front  : q[0]
back   : q[-1]
'''
from collections import deque
import sys

input = sys.stdin.readline

# 명령의 수 N (1 ≤ N ≤ 10,000) 입력
N = int(input())

# 큐 사용
q= deque()

# 명령어 수행
for _ in range(N):
  # 명령어 입력
  command = input()
  
  # push
  if "push" in command:
    comm, x = command.split()
    q.append(int(x))
  # pop
  elif "pop" in command:
    print(q.popleft()) if q else print(-1)
  # size
  elif "size" in command:
    print(len(q))
  # empty
  elif "empty" in command:
    print(0) if len(q) else print(1)
  # front
  elif "front" in command:
    print(q[0]) if q else print(-1)
  # back
  elif "back" in command:
    print(q[-1]) if q else print(-1)