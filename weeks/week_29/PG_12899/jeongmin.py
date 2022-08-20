def solution(n):
    answer = ""
    
    # 3으로 나눈 나머지 기준으로 1, 2, 4로 바꾸기
    numbers = ['4', '1', '2']
    
    while n>0:
        answer += numbers[n%3]  
        n = (n-1)//3    
 
    answer = answer[::-1]   # 순서 뒤집기
    
    return answer