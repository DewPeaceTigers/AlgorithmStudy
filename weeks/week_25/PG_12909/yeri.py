def solution(string):
    string = list(string)
    stack=[]
    
    for s in string:
        if not stack:
            if s=='(':
                stack.append(s)
            else: return False
            continue
        if s =='(':
            stack.append(s)
        else:
            if stack[-1]=='(':
                stack.pop()
            else:
                break
    if stack: return False
    else: return True