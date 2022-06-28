def solution(n):
    ans = 1
    
    while n!=1:
        if n%2==0 : #짝수이면 순간이동하면 됨
            n/=2
        else:
            n-=1 #한번에 5칸 점프나 한칸씩 5번 이동이나 소비량은 동일
            ans+=1
    
    return ans