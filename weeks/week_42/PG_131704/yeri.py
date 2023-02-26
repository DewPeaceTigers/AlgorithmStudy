from collections import deque
def solution(order):
    main = deque([i for i in range(1,len(order)+1)])
    sub = []
    now = 0
    
    while main and now < len(order):
        if main[0] == order[now]:
            main.popleft()
            now+=1
        elif sub and sub[-1] == order[now]:
            sub.pop()
            now+=1
        else:
            sub.append(main.popleft())
    while sub:
        if order[now] == sub[-1]:
            now+=1
            sub.pop()
        else:
            break
    return now