def solution(brown, yellow):
    answer = []
    
    for i in range(yellow+1):
        for j in range(i, yellow+1):
            if i*j == yellow and i+j == (brown-4)//2:
                answer.append(j+2)
                answer.append(i+2)
    
    return answer