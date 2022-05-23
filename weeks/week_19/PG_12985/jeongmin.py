# 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지

def solution(n,a,b):
    answer = 0

    while a!=b:
        # round()는 사사오입 원칙을 따른다.
        # 파이썬에서 round 함수로 0.5를 반올림할 때, 
        # 정수 부분이 짝수면 반내림이 되고, 홀수면 반올림이 된다.
        a = round(a/2+0.1)  # (A) 다음 라운드 번호
        b = round(b/2+0.1)  # (B) 다음 라운드 번호
        
        # a, b = (a+1)//2, (b+1)//2     # 이렇게도 가능!
        
        answer += 1
        
    return answer