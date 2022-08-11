def solution(s):
    s= sorted(list(map(int,s.split(' '))))
    return str(s[0])+" "+str(s[len(s)-1])