from collections import deque
def solution(s):
    pairs={
        '[':']',
        '{':'}',
        '(':')'
    }
    turn =0
    count=0
    s= deque(s)
    from copy import deepcopy
    while True:
        turn+=1
        temp = deepcopy(s)
        stack=[]
        while temp:
            # 왼쪽이 들어갈 때
            if temp[0] in pairs:
                stack.append(temp.popleft())
            # 오른쪽이 들어갈 때
            else:
                if not stack : break
                elif pairs[stack[-1]] == temp[0]:
                    # 짝이 맞다면
                    stack.pop()
                    temp.popleft()
                else:
                    # 짝이 맞지 않다면
                    break
        if not temp and not stack :count+=1
        if turn==len(s): break
        s.rotate(-1)
    return count