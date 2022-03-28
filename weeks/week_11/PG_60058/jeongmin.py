def divStr(p): # u, v로 분리하기
    a, b = 0, 0
        
    for i, x in enumerate(p):
        if x=='(':
            a+=1
        else:
            b+=1
        if a==b:
            u = p[:i+1]
            v = p[i+1:]
            break
    return (u, v)

def check(p): # 올바른 문자열인지 체크
    stack = []
    
    isRight = True
    for x in p:
        if x=='(':
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                # 올바르지 않은 문자열
                isRight = False
                break
    return isRight

def recur(p):
    # 올바른 괄호 문자열
    if check(p):
        return p
    
    # 균형잡힌 괄호 문자열
    else:
        u, v = divStr(p)
        
        # u가 올바른 문자열
        if check(u):
            return u+recur(v)
          
        # u가 올바른 괄호 문자열이 아니라면
        else:
            temp = "("+recur(v)+')'
            
            # u의 앞뒤 문자 제거 & 괄호 방향 뒤집기
            for i in range(1, len(u)-1):
                temp += '(' if u[i]==')' else ')'
                
            return temp
        
def solution(p):
    
    answer = recur(p)
    
    return answer