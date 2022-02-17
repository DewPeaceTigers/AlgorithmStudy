def solution(citations):
    citations.sort() # 0 1 3 5 6
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i: # 1 >= 4(5-1) / 3 >= (5-2) 
            #정렬을 해두었으므로 i번째 뒤로는 해당 값보다 다 크다. 
            #i번째 값이 남아있는 논문 수보다 같거나 크면 i번째 값 이상 인용된 논문이 h편 이상이라는 소리다.
            return l-i
    return 0