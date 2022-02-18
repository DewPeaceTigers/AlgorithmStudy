def solution(citations):
    answer = 0
    
    citations.sort(reverse=True) # 논문의 인용 횟수가 큰 순으로 정렬
    for i in range(len(citations)): 
        if i+1<=citations[i]: # (i+1)번 이상 인용된 논문이 (i+1)편 이상
            answer=i+1 
        else: 
            break
    
    return answer