def solution(bridge_length, weight, truck_weights):

    crossing = []   # 다리를 건너는 트럭 저장
    time, w = 0, 0  # 경과 시간, 현재 다리에 있는 트럭의 무게 합
    
    while truck_weights:
        time += 1
        
        # 지나간 트럭 빼기
        if crossing and crossing[0][1] == time:
            tw, t = crossing.pop(0)
            w -= tw
        
        # weight 이하까지의 무게, 트럭이 최대 bridge_length대 올라갈 수 있음
        if w+truck_weights[0] <=weight and len(crossing)+1 <=bridge_length:
            t = truck_weights.pop(0)    # 첫번째 대기 트럭 꺼냄
            w += t          
            # 다리를 건너는 트럭에 추가 [무게, 다리를 다 건너는 시간]
            crossing.append([t, time+bridge_length])
            
    # 마지막 트럭이 다리를 건너기 시작한 시간 + 다리 길이    
    answer = time + bridge_length
    
    return answer