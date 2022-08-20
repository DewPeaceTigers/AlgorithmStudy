'''
³ª¸ÓÁö 1:1, 2:2 0:4
'''
def solution(n):
    answer = ''
    
    while(n>0) :
        if n%3==0 :
            answer+=str(4)
            n=n//3-1
        elif n%3==1 :
            answer+=str(1)
            n=n//3
        else:
            answer+=str(2)
            n=n//3
        
    return answer[::-1]