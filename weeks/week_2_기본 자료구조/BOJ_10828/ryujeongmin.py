''' [풀이]
1. sys.stdin.readline 이용하여 여러줄 입력 (input()으로 하면 시간초과)
2. 스택 - 리스트 사용
3. 조건문으로 각 명령어 확인

[명령 종류]
push X : q.append(x)
pop    : q.pop()
size   : len(q)
empty  : len(q)==0
top    : q[-1]
'''

import sys

input = sys.stdin.readline

# 명령의 수 N (1 ≤ N ≤ 10,000) 입력
N = int(input())

# 스택 사용
stack=[]

# 명령어 수행
for _ in range(N):
  # 명령어 입력
  command = input()
  
  # push
  if "push" in command:
    comm, x = command.split()
    stack.append(int(x))
  # pop
  elif "pop" in command:
    print(stack.pop()) if stack else print(-1)
  # size
  elif "size" in command:
    print(len(stack))
  # empty
  elif "empty" in command:
    print(0) if len(stack) else print(1)
  # top
  elif "top" in command:
    print(stack[-1]) if stack else print(-1)