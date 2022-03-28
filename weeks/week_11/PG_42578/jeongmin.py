# clothes 각 행 : [의상의 이름, 의상의 종류]

from collections import defaultdict

def solution(clothes):
    answer = 1
    
    # key: 의상의 종류, value: 의상의 이름 리스트
    clothes_dict = defaultdict(list)
    for c in clothes:
        name, kind = c
        clothes_dict[kind].append(name)
    
    for c in clothes_dict.values():
        # len(c)+1 : 종류별 의상 수 + 의상을 선택하지 않는 경우
        answer *= (len(c)+1)
        
    # 입은 의상이 없는 경우 한가지 제외
    answer -= 1
    
    return answer