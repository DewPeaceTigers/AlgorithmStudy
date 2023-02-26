from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    # 대기 트럭
    waiting = deque(truck_weights)
    
    # 경과 시간
    t = 0
    
    # 다리를 건너는 트럭
    crossing = deque()
    
    # 다리에 있는 무게 합
    weight_sum = 0
    
    while waiting:
        # 경과 시간 +1
        t += 1
        
        # 다리를 건넌 트럭 처리
        if crossing and crossing[0][1] + bridge_length == t:
            c = crossing.popleft()
            weight_sum -= c[0] 
                
        # 무게 합이 weight을 넘지 않는다면
        if weight_sum + waiting[0] <= weight:
            # 다리를 건넘
            truck = waiting.popleft() # 대기 트럭에서 제거
            
            crossing.append([truck, t]) # 다리를 건너는 트럭 목록에 추가
            
            weight_sum += truck # 다리를 건너는 트럭의 무게 합
                
    # 마지막 트럭이 다리를 건너기 시작한 시간 + 다리 길이    
    answer = t + bridge_length
        
    return answer