def solution(numbers) :
    answer=''
    numbers=list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True) #숫자를 3번 반복시키고 그 수를 정렬
                   
    return str(int(''.join(numbers)))