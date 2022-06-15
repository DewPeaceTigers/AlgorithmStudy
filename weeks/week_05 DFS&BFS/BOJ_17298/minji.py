import sys
'''
n=int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
NGE=[]

시간  초과
while len(arr) :
    count=0
    for i in range(0, len(arr)) :
        count+=1
        if arr[0] < arr[i] :
            NGE.append(arr[i])
            arr.pop(0)
            break
    if count==len(arr) :
        NGE.append(-1)
        arr.pop(0)
'''
n=int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

NGE=[-1 for _ in range(n)]
stack=[]
stack.append(0)
for i in range(1, n) :
    while stack and arr[stack[-1]]<arr[i] :
        NGE[stack.pop()]=arr[i]
    stack.append(i)
print(*NGE)
