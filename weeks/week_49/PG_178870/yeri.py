def solution(sequence, k):
    answer = []
    l,r = 0, len(sequence)-1
    rear = len(sequence)-1
    end = len(sequence)-1
    for i in range(len(sequence)):
        if sequence[i]>k:
            end = i
        elif sequence[i]==k:
            return [i,i]
    now = 0
    length = end+1
    for i in range(end,-1,-1):
        now += sequence[i]
        if now == k and end-i+1 <= length:
            answer = [i,end]
            length = end-i+1
        elif now > k:
            now -= sequence[end]
            end-=1
            if now == k:
                answer = [i,end]
                length = end-i+1
                
    return answer