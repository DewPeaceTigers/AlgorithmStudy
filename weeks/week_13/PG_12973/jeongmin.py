def solution(s):
    
    # 짝을 찾기 위한 배열 사용
    res = [s[0]]
    
    for x in s[1:]:
        # 마지막 배열 값과 x값이 같으면 배열에서 pop
        if res and res[-1] == x:
            res.pop()
        else:
            res.append(x)
    
    # 모두 제거할 수 있다면 res는 빈 배열
    answer = 0 if res else 1
    
    return answer