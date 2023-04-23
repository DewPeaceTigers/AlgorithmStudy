""" 스택 활용.. 풀이 참고 """

# 건물 리스트에서 건물을 하나씩 빼서
# 스택에 해당 건물보다 높이가 작으면 스택에서 pop()하고
# 크면 stop하고 해당 건물을 스택에 append 한다
# 위 과정을 거친 후에 stack의 길이에서 1을 뺀 값을 result 변수에 더해줌

import sys 

input = sys.stdin.readline 

N = int(input())

buildings = [int(input()) for _ in range(N)]

stack = []
result = 0

for b in buildings:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)

    result += len(stack)-1

print(result)