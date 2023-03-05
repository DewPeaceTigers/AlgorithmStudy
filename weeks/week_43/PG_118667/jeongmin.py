def solution(queue1, queue2):
    answer = -1
    
    # 각 큐의 원소 합
    sum1, sum2 = sum(queue1), sum(queue2)

    k = (sum1+sum2)//2
    
    # 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수
    cnt = 0
    
    # 두 큐를 합친 큐
    q = queue1 + queue2
    l = len(q)
    
    # 투 포인터 사용
    s, e = -1, len(queue1)-1
    while s<e and e<2*l:
        if sum1 == k:
            answer = cnt
            break 
        elif sum1 < k:
            e += 1
            sum1 += q[e%l]
        else:
            s += 1
            sum1 -= q[s%l]
        cnt += 1
    
    return answer