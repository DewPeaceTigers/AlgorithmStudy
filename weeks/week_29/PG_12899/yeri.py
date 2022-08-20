def solution(n):
    nums=[1,2,4]
    answer=''
    while n!=0:
        n,idx = divmod(n-1,3) # n-1인 이유는 1이 아니라 0부터 시작하기 때문에
        answer = str(nums[(idx)%3])+answer
    return answer