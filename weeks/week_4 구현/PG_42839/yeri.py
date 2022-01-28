from itertools import permutations
import math
def checkPrime(n): # 소수 찾기 - 에라토스테네스의 체를 사용하려 했으나 여러 수를 판별할 땐 별로라 해석 급히 우회함..
    n=int(n)
    print(math.sqrt(n),n**0.5)
    if n==0 or n==1: return False
    for i in range(2,int(n**0.5)):
        if n%i==0: return False
    return True
def solution(numbers): 
    answer = set()
    numbers=list(numbers)
    for i in range(1,len(numbers)+1):
        combs=list(permutations(numbers,i)) # i개수 만큼 순열 만들기
        for comb in combs: # 각 순열 마다 돌면서 문자열로 만들어주기
            num=''
            for c in comb:
                num+=c
            if checkPrime(int(num)): answer.add(int(num)) # 만든 문자열이 소수면 answer에 저장하기

    return len(answer) # 이때 answer은 set이기 때문에 중복을 거른 상태.
print(solution('17'))
print(solution('011'))