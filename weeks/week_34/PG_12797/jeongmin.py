import math

def solution(n, stations, w):
    answer = 0

    # 전파가 도달하지 않는 구간 저장
    area = []
    
    ns = len(stations)
    
    for i in range(ns):
        if i==0 and stations[0]>w+1:
            area.append((1, stations[0]-w-1))
        if i== ns-1 and stations[-1]<n-w:
            area.append((stations[-1]+w+1, n))
        
        if i<ns-1 and stations[i]+w < stations[i+1]-w:
            area.append((stations[i]+w+1, stations[i+1]-w-1))
            
    for s, e in area:
        answer += math.ceil((e-s+1)/(2*w+1))

    return answer