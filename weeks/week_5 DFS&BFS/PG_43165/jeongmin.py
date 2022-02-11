'''[풀이]
dfs 사용 
부분집합 구하는 방식을 이용하여 더하기, 빼기 가능한 모든 경우의 수 확인
'''

ans = 0
def dfs(v, ch, l, numbers, target):
    global ans
    if v==l:
        sum=0
        for i in range(l):
            if ch[i]==1:
                sum+=numbers[i] # 더하기
            else:
                sum-= numbers[i] # 빼기
        if sum==target: # 연산을 한 값이 타겟넘버와 일치하는 경우
            ans+=1
        return
    
    ch[v]=1
    dfs(v+1, ch, l, numbers, target) 
    ch[v]=0
    dfs(v+1, ch, l, numbers, target) 

def solution(numbers, target):
    l = len(numbers) 
    ch = [0]*l # 더하기(1), 빼기(0) 구분용 리스트
    
    # 1<= target <= 1000 , 자연수 
    dfs(0, ch, l, numbers, target)
    answer = ans
    
    return answer