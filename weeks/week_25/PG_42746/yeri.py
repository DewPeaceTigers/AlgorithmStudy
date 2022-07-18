def solution(numbers):
    change_numbers=[]
    for num in numbers:
        temp = ''.join(list(str(num)*4)[:4])
        change_numbers.append((temp,str(num)))
    change_numbers.sort(reverse=True)
    answer=''
    for _,cn in change_numbers:
        answer+=cn
    
    return answer if int(answer)!=0 else "0"