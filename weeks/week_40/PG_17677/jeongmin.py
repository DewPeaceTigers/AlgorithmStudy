def solution(str1, str2):
    answer = 0
    
    # 문자열 소문자로 통일
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 문자열 길이
    l1, l2 = len(str1), len(str2)
    
    multi_set = dict()
    # 두 글자씩 끊어서 다중 집합의 원소 만들기
    for i in range(l1-1):
        tmp = str1[i:i+2]
        
        # 영문자로 된 글자쌍만 유효함!
        if not tmp.isalpha():
            continue
            
        if tmp in multi_set:
            multi_set[tmp][0] += 1
        else:
            multi_set[tmp] = [1, 0]

    for i in range(l2-1):
        tmp = str2[i:i+2]
        
        # 영문자로 된 글자쌍만 유효함!
        if not tmp.isalpha():
            continue
        
        if tmp in multi_set:
            multi_set[tmp][1] += 1
        else:
            multi_set[tmp] = [0, 1]
        
    # 교집합, 합집합 개수 세기
    intersection, union = 0, 0
    for key, value in multi_set.items():
        intersection += min(value)
        union += max(value)
    
    if union == 0: # 나눗셈이 정의되지 않는 경우
        answer = 65536
    else:
        answer = int(intersection/union*65536)

    return answer