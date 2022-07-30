def solution(n):
    answer = 1 #n인 경우 15=15
    for i in range(1, n+1) :
        sum=i
        for j in range(i+1, n+1) : #i다음 숫자부터 하나씩 더했을 때
            sum+=j
            if sum==n : #n이 나오면 +1
                answer+=1
                break
            elif sum>n : #n보다 크면 종료
                break
            
    return answer