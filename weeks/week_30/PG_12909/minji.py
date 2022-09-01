def solution(s):
    stack=[]
    for i in range(len(s)) :
        if s[i]=="(" :
            stack.append(s[i])
        else:
            if len(stack)==0:
                return False
            stack.pop()
    if len(stack)==0:
        return True
    else:
        return False