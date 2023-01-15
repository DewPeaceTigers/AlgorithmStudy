from collections import deque

def solution(priorities, location):
    # 요청한 문서가 몇번째로 출력되는지
    answer = 0
    
    # 대기목록
    q = deque([(i, priorities[i]) for i in range(len(priorities))])

    while q:
        # 가장 앞에 있는 문서 꺼냄
        idx, p = q.popleft()

        # 나머지 인쇄 목록 중 중요도가 높은 문서가 한 개라도 존재하면
        if any (p<x[1] for x in q):
            # 대기 목록의 마지막에 넣음
            q.append((idx, p))
            continue
        
        answer += 1
        # 요청한 문서가 인쇄되는 경우
        if idx==location:
            break
    
    return answer