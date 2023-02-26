"""
정규표현식 사용
- 정규식 "a.b" => "a + 모든문자 + b"
"""


import re
from itertools import permutations 

def solution(user_id, banned_id):
    n = len(banned_id)
    
    # 불량 사용자 아이디의 *를 .로 변경
    banned_id = [i.replace("*", ".") for i in banned_id]
    
    # 제재 아이디 목록 저장
    answer = []

    # 모든 순열 조합 확인
    for case in permutations(user_id, n):
        users = list(case)
        flag = True
        
        for j in range(n):
            # 불량 사용자 목록에 매핑됨
            # 길이 체크 필요! ("acbc"도 "a.b"랑 match 한다고 나옴)
            if re.match(banned_id[j], users[j]) and (len(banned_id[j]) == len(users[j])):
                continue 
            # 불량 사용자 목록에 매핑 안됨
            else:
                flag = False
                break
        if flag:
            if sorted(users) not in answer:
                answer.append(sorted(users))

    return len(answer) 
