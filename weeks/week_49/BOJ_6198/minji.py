import sys

input=sys.stdin.readline

n=int(input())
heights=[int(input()) for _ in range(n)]

ans=0
stack=[]

for i in range(n) : #10 3 7 4 12 2
    while stack and stack[-1]<=heights[i] :
        stack.pop()
    stack.append(heights[i])
    ans+=(len(stack)-1)

print(ans)