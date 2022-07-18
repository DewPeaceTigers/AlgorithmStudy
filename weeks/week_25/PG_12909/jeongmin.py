def solution(s):
    stack = []
    for x in s:
        if x=='(':
            stack.append(x)
        else:
            if not stack:
                return False
            stack.pop()
    
    # '('가 남은 경우
    if stack:
        return False

    return True