def solution(n):
    answer = []
    def hanoi(cnt,start,end,sub):
        if(cnt==1):
            answer.append([start,end])
            return
        hanoi(cnt-1,start,sub,end)
        answer.append([start,end])
        hanoi(cnt-1,sub,end,start)
    hanoi(n,1,3,2)
    return answer