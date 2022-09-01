def solution(queue1, queue2):
    # pop하지 않고 맨 첫의 인덱스를 움직이기 -> 어차피 앞에서 빼서 뒤에 붙이는 일만 함
    answer = -1
    sum1=sum(queue1)
    sum2=sum(queue2)
    target=(sum1+sum2)//2
    i,j,t=0,0,len(queue1)
    while i<2*t and j<2*t and sum1!=sum2:
        if sum1<target:
            sum1+=queue2[j]
            sum2-=queue2[j]
            queue1.append(queue2[j])
            j+=1
        else:
            sum2+=queue1[i]
            sum1-=queue1[i]
            queue2.append(queue1[i])
            i+=1
    if sum1 == target:
        answer = i+j
    return answer