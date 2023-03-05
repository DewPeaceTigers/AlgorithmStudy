def solution(queue1, queue2):
    answer=0
    q1 = sum(queue1)
    q2 = sum(queue2)
    length = len(queue1)
    
    i1 = 0
    i2 = 0
    while q1!=q2 and i1<length*2 and i2<length*2:
        answer+=1
        if q1>q2:
            f = queue1[i1]
            q1-=f
            q2+=f
            queue2.append(f)
            i1+=1
        else:
            f = queue2[i2]
            q2-=f
            q1+=f
            queue1.append(f)
            i2+=1
    return answer if q1==q2 else -1