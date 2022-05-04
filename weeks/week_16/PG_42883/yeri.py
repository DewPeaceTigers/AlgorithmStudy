def solution(number, k):
    answer = ''
    result_len = len(number)-k
    pivot = 0
    while(result_len>0):
        until = len(number)-result_len+1
        if len(number)-pivot == result_len : 
            answer+=number[pivot:]
            break
        current_max='0'
        for n in range(pivot,until):
            if current_max < number[n]: 
                current_max=number[n]
                pivot = n
                if number[n]=='9': break
        #current_max = max(number[pivot:until]) #max 직접 구현하기
        answer+=current_max
        pivot +=1 #number[pivot:until].find(current_max)+pivot+1
        result_len-=1
    return answer