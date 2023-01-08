import re
from collections import deque
from itertools import permutations

def calc(n1, n2, op):
    if op=='+':
        return n1+n2
    elif op=='-':
        return n1-n2
    elif op=='*':
        return n1*n2

def solution(expression):
    answer = 0
    
    expression = re.split('([-|+|*])', expression)
    # 숫자는 정수형으로 변환
    for i in range(len(expression)):
        if i%2==0:
            expression[i] = int(expression[i])
    
    # 모든 우선순위 조합 확인
    for case in permutations(['+', '-', '*'], 3):
        q = deque(expression)
        
        # 우선순위대로 연산 수행
        for i in range(3):
            nq = []
            
            while q:
                x = q.popleft()
                
                # x가 우선순위에 해당하는 연산문자인 경우
                if x==case[i]:
                    # 연산 수행
                    x = calc(nq.pop(), q.popleft(), x)
                
                nq.append(x) 
            
            q = deque(nq)
            
        
        answer = max(answer, abs(q[0]))
            
    return answer