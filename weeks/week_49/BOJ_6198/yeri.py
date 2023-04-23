import sys
input = sys.stdin.readline

N = int(input())
buildings = list(map(int,input().split()))

# 현재 옥상을 볼 수 있는 숫자를 구함 (어차피 합계임) 다시!
stack = []
result = 0

for b in buildings:
  while stack and stack[-1]<=b:
    stack.pop()
  stack.append(b)

  result += len(stack)-1
