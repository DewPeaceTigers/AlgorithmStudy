"""
n-튜플(n-tuple)

return: 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플
"""

def solution(s):
    answer = []
    s = s[2:-2].split('},{')        # 집합 구분하기
    s.sort(key = lambda x: len(x))  # 집합 길이순으로 정렬
    
    for x in s:
        # 집합 원소
        num = x.split(',')

        # 중복되는 원소가 없도록 추가
        for n in num: 
            if int(n) in answer:
                continue
            answer.append(int(n))
    
    return answer