
def solution(brown, yellow):
    answer=[0,0]
    sum = brown+yellow
    for i in range(1,sum//2+1):
        if sum%i==0:
            j = sum//i
            if (i-2)*(j-2) == yellow:
                answer=[j,i]
                break
    return answer