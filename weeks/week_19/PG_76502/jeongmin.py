# s가 올바른 문자열이 되게 하는 x의 개수
bracket = {'(':')', '[':']', '{':'}'}

# 올바른 괄호 문자열인지 체크
def check(s):
    stack=[]
    
    for c in s:
        # 여는 괄호
        if c in ('(', '[', '{'):
            stack.append(c)
        # 닫는 괄호
        else:
            # 닫는 괄호가 먼저 나온 경우
            if not stack:
                return False
        
            # 괄호 짝이 맞지 않는 경우
            elif bracket[stack.pop()] != c:
                return False
        
    # 남은 괄호가 있는 경우
    if stack:
        return False
    
    return True
    

def solution(s):
    answer = 0
    
    for x in range(len(s)):
        # s를 왼쪽으로 x칸 만큼 회전
        ns = s[x:] + s[:x]
        
        # 올바른 괄호 문자열인지 확인
        if check(ns):
            answer += 1
          
    return answer