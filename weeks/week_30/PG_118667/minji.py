from collections import deque

def solution(queue1, queue2):
    answer = -1
    q1=deque(queue1)
    q2=deque(queue2)
    sum1=sum(queue1)
    same_sum=(sum1+sum(queue2))//2
    count=0
    while q1 and q2 :
        if sum1==same_sum:
            return count
        elif sum1>same_sum :
            sum1-=q1.popleft()
        elif sum1<same_sum :
            q1.append(q2.popleft())
            sum1+=q1[-1]
        count+=1
        
    return answer
