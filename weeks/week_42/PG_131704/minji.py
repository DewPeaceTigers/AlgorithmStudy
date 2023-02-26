def solution(order):
    stack=[]
    i=1
    now=0

    while i!=len(order)+1 :
        stack.append(i)
        while stack[-1]==order[now] :
            now+=1
            stack.pop()

        i+=1

    return now