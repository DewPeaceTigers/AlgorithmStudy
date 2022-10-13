def solution(s):
   
    answer = 0
    
    pair = [s[0]]
    
    for i in range(1, len(s)):
        if pair and pair[-1] == s[i]:
            pair.pop()
        else:
            pair.append(s[i])

    # 문자열이 모두 제거된 경우 -> 짝지어 제거하기 성공적으로 수행
    answer = 1 if not pair else 0
    
    return answer