def solution(s):
    # 이진 변환의 횟수, 변환 과정에서 제거된 모든 0의 개수
    answer = [0, 0]

    while s != "1":
        # 원래 길이
        l = len(s)
        
        # 모든 0 제거한 후의 길이
        c = len(s.replace("0", ""))
    
        # c를 2진법으로 표현한 문자열
        s = bin(c)[2:]
    
        answer[0] += 1
        # 제거된 0의 수 저장
        answer[1] += (l-c)
        
    return answer