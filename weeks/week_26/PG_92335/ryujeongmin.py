"""
소수인지 판별할 때

- 2~n**(0.5) 까지 순회하면서 나누어떨어지는지를 확인하면 됨!
"""

def convert(n, k):
    num = ''
    
    while n>0:
        num += str(n%k)
        n//=k
    
    return num[::-1]


def isPrime(n):
    if n==1:
        return False
    
    size = int(n**(1/2))+1
    
    for i in range(2, size):
        if n%i==0:
            return False
    
    return True

def solution(n, k):
    answer = 0
    
    # 진법 변환 후 '0'으로 숫자 나누기
    nums = convert(n, k).split('0')
    
    # 소수인지 확인
    for x in nums:
        if x!='' and isPrime(int(x)):
            answer +=1

    return answer