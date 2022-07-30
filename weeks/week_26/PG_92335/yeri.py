import math
def make(n,r):
    temp=[]
    while n:
        left,n = n%r, n//r;
        temp.append(str(left))
    return ''.join(temp[::-1])
def check(num):
    if num==1: return False
    if num==2: return True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0: return False
    return True
def solution(n, k):
    answer = 0
    nums = make(n,k).split('0')
    for num in nums:
        if not num: continue
        if check(int(num)):
            answer+=1
    return answer