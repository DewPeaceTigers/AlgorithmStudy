def solution(queue1, queue2):
    answer = 0
    q1 = 0
    q2 = 0
    length = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    while sum1!=sum2 and q1 < length*2 and q2<length*2:
        answer+=1
        if sum1 < sum2:
            f = queue2[q2]
            q2+=1
            sum1+= f
            sum2-= f
            queue1.append(f)
        else :
            f = queue1[q1]
            q1+=1
            sum2+= f
            sum1-= f
            queue2.append(f)
    return answer if sum1==sum2 else -1