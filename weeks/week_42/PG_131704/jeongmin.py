from collections import deque

def solution(order):
    answer = 0
    
    N = len(order)
    
    visited = [False] * (N+1)
    
    # 컨테이너 벨트
    container = deque(range(1, N+1))
    
    # 보조 컨테이너
    sub_container = [0]
    
    i = 0
    while i<N:  
        # 컨테이너 맨 앞에 놓인 상자가 현재 트럭에 실어야 하는 순서인 경우
        if container and container[0] == order[i]:
            container.popleft()
            i += 1
            answer += 1
            continue
        
        # 보조 컨테이너 맨 마지막에 보관한 상자 확인 
        if sub_container[-1] == order[i]:
            sub_container.pop()
            i += 1
            answer += 1
            continue
        
        # 보조컨테이너 앞쪽에 있는 상자인 경우는 불가능
        if visited[order[i]]:
            break
        
        # 보조 컨테이너에 상자 넣기
        x = container.popleft()
        sub_container.append(x)
        visited[x] = True        
    
    
    return answer