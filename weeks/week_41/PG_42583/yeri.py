from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weights = deque(truck_weights)
    bridge_total = 0
    bridge = deque([0]*bridge_length)
    while truck_weights: 
        answer+=1
         
        bye = bridge[0]
        bridge[0] = 0
        bridge.rotate(-1)
        bridge_total-=bye
        
        hello = truck_weights[0]
        if bridge_total+hello <= weight:
            bridge_total+=hello
            bridge[-1] = truck_weights.popleft()
    if bridge_total!=0:
        answer+=bridge_length
            
    return answer