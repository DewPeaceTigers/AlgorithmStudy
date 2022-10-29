n, k=map(int, input().split())
numbers=input().rstrip()

stack=[]
for number in numbers :
    while stack and k>0 and stack[-1]<number:
        stack.pop()
        k-=1
    stack.append(number)

if k>0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
