"""
메뉴 조합 -> 코스 요리

코스요리 메뉴구성
- 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품 메뉴들
- 최소 2가지 이상
- 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합

"""
from itertools import combinations

def solution(orders, course):
    answer = []
    
    case = [dict() for i in range(11)]
    order = [list(o) for o in orders]
        
    # 코스요리를 구성하는 단품메뉴들의 갯수별 메뉴 조합 구하기
    for c in course:
        for i, o in enumerate(order):
            # 메뉴 조합 구하기 
            comb = combinations(o, c)
            for com in comb:
                s_dict = "".join(sorted(com))
                if s_dict not in case[c]:
                    case[c][s_dict]=1
                else:
                    case[c][s_dict]+=1
    
        s_case = list(zip(case[c].keys(),case[c].values()))
        s_case.sort(key=lambda x:x[1], reverse=True)
        
        if s_case:
            m = s_case[0][1]
            
            # 주문한 손님이 1명 이하인 경우
            if m<=1:
                continue
            
            for x in s_case:
                if x[1]<m:
                    break
                answer.append(x[0])
        
    answer.sort()
    
    return answer