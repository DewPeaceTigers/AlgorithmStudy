import sys

input = sys.stdin.readline

N, K = map(int, input().split())

nums = input().rstrip()

stack = []

for num in nums:
    while stack and stack[-1] < num and K > 0:
        stack.pop()
        K -= 1
    stack.append(num)

if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))