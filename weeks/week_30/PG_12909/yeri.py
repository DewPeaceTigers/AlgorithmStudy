def solution(string):
    stack=[]
    for s in string:
        if not stack:
            stack.append(s)
        else:
            if s==")" and stack[-1]=="(":
                stack.pop()
            if s=="(":
                stack.append(s)
    if stack: return False
    else: return True