from collections import deque
from copy import deepcopy
def solution(p):
    p = deque(list(p))
    def isLeft(s):
        if s=="(": return True
        return False
    def correct(p):
        if not p : return ''
        left=0
        right=0
        # 균형 잡힌 문자열
        u=deque([])
        while p :
            top=p.popleft()
            if isLeft(top): left+=1
            else : right+=1
            u.append(top)
            if left==right: break
        v= deepcopy(p)

        # 올바른지
        stack=[]
        is_wrong=False
        for i in range(len(u)):
            if isLeft(u[i]):
                stack.append(u[i])
            else:
                # stack이 비었다면 올바르지 않음 break
                if not stack:
                    is_wrong=True
                    break
                else:
                    if not isLeft(stack[-1]):
                        is_wrong = True
                        break
        v = correct(v)
        if is_wrong:
            temp = ['(']
            temp.extend(v)
            temp.append(')')
            # 맨 앞과 맨 뒤 문자열 지우기
            u.popleft()
            u.pop()
            for i in range(len(u)):
                u[i]= ')' if u[i]=='(' else '('
            temp.extend(u)
            #temp.append(')')
            u=temp
            return ''.join(temp)
        else:
            return ''.join(u)+''.join(v)

    return correct(p)