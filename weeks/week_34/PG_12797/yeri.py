def solution(n, stations, w):
    answer = 0
    idx = 0
    si = 0
    while idx<n:
        if si!=len(stations):
            if idx < stations[si]-w-1:
                answer+=1
                idx+=2*w+1
            elif idx<stations[si]+w:
                idx=stations[si]+w
                si+=1
        else:
            answer+=1
            idx+=2*w+1
    return answer