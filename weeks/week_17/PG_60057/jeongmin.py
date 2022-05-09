"""
비손실 압축 방법
- 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘
- 단점 : 반복되는 문자가 적은 경우 압축률이 낮다
- 해결 방법 : 1개 이상의 단위로 잘라서 압축

출력 : 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이

"""

def solution(s):
    n = len(s)
    answer = n
    
    # 1개 이상 n//2개 이하 단위로 문자열을 잘라 압축하는 경우 확인
    for unit in range(1, n//2+1):
        ns = "" # 압축 문자열 저장
        
        cnt = 1 # 횟수
        part = s[:unit] # 단위로 자른 문자열 (첫번째)

        for i in range(1, n//unit):
            # 다음 문자열
            npart = s[unit*i:unit*(i+1)]    
            
            # 이전 문자열과 같으면
            if part == npart:
                cnt += 1    # 나타난 횟수 증가
                continue
                
            # 이전 문자열과 다르면          
            if cnt > 1:     # 두 번 이상 나타난 경우 숫자 추가
                ns += str(cnt)
            ns += part      # 반복되는 문자 추가
            
            cnt = 1         # 횟수 초기화
            part = npart    
            # print(ns)
            
        # 마지막 남은 문자열 붙여주기
        if cnt > 1:
            ns += str(cnt)
        ns += s[unit*i:]

        # 짧은 것의 길이를 저장 
        answer = min(answer, len(ns))
    
    return answer