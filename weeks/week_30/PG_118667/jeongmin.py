def solution(queue1, queue2):
    answer = -2
    
    queue = queue1 + queue2
    L = len(queue)
    target = sum(queue)//2
    
    s, e = 0, L//2
    q1Sum = sum(queue1)
    
    while s<e:
        # print(q1Sum, s, e)
        if s//L > 0:
            break
            
        if q1Sum == target:
            break
        
        elif q1Sum < target:
            q1Sum += queue[e%L]
            e += 1
        
        else:
            q1Sum -= queue[s%L]
            s += 1
           
    if q1Sum!= target:
        answer = -1
    else:
        answer = s + e - L//2
    return answer