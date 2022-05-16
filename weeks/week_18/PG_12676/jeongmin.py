"""
자카드 유사도 : J(A, B)
- 집합 간의 유사도를 검사하는 여러 방법 중의 하나
- 두 집합 A, B의 교집합 크기 / 두 집합의 합집합 크기
- 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의함
- 원소의 중복을 허용하는 다중집합에 대해서 확장 가능

- 0 < 유사도(answer) <= 1 
"""

from collections import defaultdict

def solution(str1, str2):
    answer = 0
    
    a = str1.lower()
    b = str2.lower()
    
    # 다중집합 저장 {'글자쌍': [A의 개수, B의 개수]}
    # 집합 A, B에서 해당 글자쌍이 나오는 개수 저장
    jacad = dict()
    
    # 두 글자씩 끊어서 다중 집합 만들기 (A)
    for i in range(len(a)-1):
        twoStr = "".join(a[i:i+2])
        # 영문자로 된 글자 쌍만 저장
        if twoStr.isalpha(): 
            if twoStr in jacad:
                jacad[twoStr][0]+=1
            else:
                jacad[twoStr]= [1, 0]

    # 두 글자씩 끊어서 다중 집합 만들기 (B)
    for i in range(len(b)-1): 
        twoStr = "".join(b[i:i+2])
        # 영문자로 된 글자 쌍만 저장
        if twoStr.isalpha():
            if twoStr in jacad:
                jacad[twoStr][1] += 1
            else:
                jacad[twoStr]= [0, 1]
    
    # 집합 A 와 집합 B가 모두 공집합인 경우
    if len(jacad) == 0:
        answer = 65536
        
    else:
        # 교집합 개수 # 합집합 개수
        intersect, union = 0, 0

        # 만들어진 글자쌍 확인
        for v in jacad.values():
            intersect += min(v) # 교집합 : 최솟값
            union += max(v)     # 합집합 : 최댓값
            
        answer = int(intersect/union*65536)
    
    return answer