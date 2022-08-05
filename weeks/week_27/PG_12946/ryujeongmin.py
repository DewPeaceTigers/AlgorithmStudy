answer = []

def hanoi(n, s, t, e):
    if n==0:
        return 
    
    hanoi(n-1, s, e, t)
    answer.append([s, e])
    hanoi(n-1, t, s, e)
    

def solution(n):
    hanoi(n, 1, 2, 3)
    return answer