import sys
from collections import deque
input = sys.stdin.readline

text = input().rstrip()
bomb = list(input().rstrip())
b = len(bomb)
# while True:
#     new_text = deque()
#     isBomb = False
#     while text:
#         if bomb == list(text)[:b]:
#             text = deque(list(text)[b:])
#             isBomb = True
#         else:
#             new_text.append(text.popleft())
#     text = new_text
#     if not isBomb : break
stack = []
for t in text:
    stack.append(t)
    if b<=len(stack) and stack[len(stack)-b:]==bomb:
        for i in range(b):
            stack.pop()
print(''.join(stack) if stack else "FRULA")