from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    time=0
    bridge_sum = 0
    while True:
        # 맨 앞 내보내기
        bridge_sum-=bridge[0]
        bridge[0]=0
        bridge.rotate(-1)
        if truck_weights and bridge_sum+truck_weights[0]<=weight:
            # 더 태울 수 있다면
            next = truck_weights.pop(0)
            bridge[-1]=next
            bridge_sum+=next
        time+=1
        if bridge_sum==0:
            break
    return time