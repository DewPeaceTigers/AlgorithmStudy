## fail

# N=int(input())
# A=deque(map(int,input().split()))
# recents=deque([A.pop()])
# res=deque([-1])
# while A:
#     rear=A.pop()
#     found=False
#     for recent in recents:
#         if rear < recent:
#             res.appendleft(recent)
#             found=True
#             break
#     if not found : res.appendleft(-1)
#     if len(A)!=0 and A[-1]< rear:
#             recents.appendleft(rear)
# print(*res)

import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0) # 첫 번째 index
for i in range(1, n): # 비교
    while stack and A[stack[-1]] < A[i]: # while 대신 if는 안되나?
        answer[stack.pop()] = A[i] # 해당 자리에 오큰수 넣기
    stack.append(i) # 다음 인덱스 비교 대상으로 올리기


print(*answer)