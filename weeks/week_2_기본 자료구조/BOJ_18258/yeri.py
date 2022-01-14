import sys
N = int(sys.stdin.readline())
stack=[]
cnt=0 #pop 하지 않고 배열의 갯수를 늘린다. pop(0)이 시간 소모가 크기 때문
for _ in range(N):
    order = sys.stdin.readline().split() # input이 많기 때문에  (1 ≤ input ≤ 10,000) 입력 받는데서 시간초과 났다.
    if order[0]=='push': # push는 split으로 x를 찾는다.
        stack.append(order[1])
    elif order[0]=='pop': # order 하나씩 확인하면서 해당 작업 해주기.
        if len(stack)-cnt==0:
            print(-1)
            continue
        print(stack[cnt])
        cnt+=1
    elif order[0]=='size':
        print(len(stack)-cnt)
    elif order[0]=='empty':
        print(1 if len(stack)-cnt==0 else 0)
    elif order[0]=='front':
        if len(stack)-cnt==0:
            print(-1)
            continue
        print(stack[cnt])
    elif order[0]=='back':
        if len(stack)-cnt==0:
            print(-1)
            continue
        print(stack[-1])