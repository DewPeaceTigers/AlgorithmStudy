def solution(s):
    answer = ''
    
    n = list(map(int, s.split()))
    n.sort()
    
    answer = str(n[0])+ " "+ str(n[-1])
    
    return answer