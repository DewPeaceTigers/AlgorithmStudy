def solution(priorities, location):
    answer = 0
    queue = [(i, q) for i, q in enumerate(priorities)]
    
    while True:
        cur = queue.pop(0)
        # 나머지 인쇄 대기목록에 중요도가 높은 문서가 하나라도 존재하면
        if any(cur[1]< q[1] for q in queue):
            # 대기목록의 가장 마지막에 추가
            queue.append(cur)
        else:
            answer +=1 # 몇변째 출력인지 나타냄
            # 인쇄를 요청한 문서
            if cur[0] ==location:
                return answer