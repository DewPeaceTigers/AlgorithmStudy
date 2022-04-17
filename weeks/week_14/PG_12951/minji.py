def solution(s):
    answer = ''
    s=s.lower()
    s=s.split(' ') #공백문자가 연속해서 나올 수 있어서
    for i in range(len(s)) :
        s[i]=s[i].capitalize() #앞글자 대문자
    answer=' '.join(s)
    return answer