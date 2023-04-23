# 후보키 
# 유일성 & 최소성 만족
from itertools import combinations

def solution(relation):
    
    row = len(relation)
    col = len(relation[0])
    
    # 가능한 속성의 모든 인덱스 조합
    case = []
    for i in range(1, col+1):
        case.extend(combinations(range(col), i))

    # 유일성 
    candidate = []
    for i in case:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        
        # print(tmp)
        
        # 유일성 확인
        if len(set(tmp)) == row:
            minimality = True
            
            for x in candidate:
                # 최소성 확인
                if set(x).issubset(set(i)):
                    minimality = False
                    break
            
            if minimality: candidate.append(i)
            
    answer = len(candidate)
    return answer