import math

def solution(n, m, section):
    answer = 1
    
    # 페인트를 칠하기로 정한 구역 번호 수
    L = len(section)
    
    # 롤러로 페인트칠하는 시작점 저장
    start = section[0]
    for i in range(1, L):
        # 롤러로 페인트칠을 한 구역 내에 있다면 넘어감
        if start + m > section[i]:
            continue
        
        # 롤러로 페인트칠하는 횟수 추가
        answer += 1
        start = section[i]
    
    return answer