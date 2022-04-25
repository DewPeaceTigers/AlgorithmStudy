# 답 찾아봄..
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
    unique = []
    for i in case:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        
        print(tmp)
        
        if len(set(tmp)) == row:
            cand = True
            
            for x in unique:
                if set(x).issubset(set(i)):
                    cand = False
                    break
            
            if cand: unique.append(i)
            
    answer = len(unique)
    return answer