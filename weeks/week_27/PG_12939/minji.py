def solution(s):
    answer = ''
    s=s.split()
    numbers=[]
    for num in s :
        if num[0]=='-' :
            numbers.append(int(num[1:])*(-1))
        else:
            numbers.append(int(num))
    answer=str(min(numbers))+" "+str(max(numbers))
    return answer