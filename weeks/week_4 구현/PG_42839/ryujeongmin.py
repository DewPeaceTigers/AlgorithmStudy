# 흩어진 종이 조각을 붙여 소수를 몇개 만들 수 있는지
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    
    for i in range(1, len(numbers)+1):
        dfs(numbers, '', i)

    isPrime = prime(max(set(nums)))
    # print(max(set(nums)), isPrime)
    for n in set(nums):
        if isPrime[n]:
            answer+=1
    
    return answer

# 소수인지 체크
def prime(n):
    isPrime = [True]*(n+1)
    isPrime[0], isPrime[1]= False, False
    
    if n==0 or n==1:
        return 
    
    for i in range(2, int(n**(1/2))+1):
        j=2
        while i*j<n+1:
            if isPrime[i*j]:
                isPrime[i*j]=False
            j+=1
    
    # print("소수 확인", n, isPrime[n])
    return isPrime

idx=[]
nums=[]
# 숫자 카드로 만들 수 있는 모든 숫자 확인
# 1개 ~ N개 로 이루어짐
def dfs(numbers, s, x):
    
    if len(idx)==x:
        # print(x, idx, int(s))
        nums.append(int(s))

        return int(s)
    
    for i in range(len(numbers)):
        if i not in idx:
            s += numbers[i] # 문자 추가
            idx.append(i)
            dfs(numbers, s, x)
            s = s[:-1] # 추가했던 문자 지우기,,
            idx.pop()