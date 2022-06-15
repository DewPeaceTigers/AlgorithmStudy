import math
def isPrime(n):
    if n==1 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0 : return False
    return True
M=int(input())
N=int(input())
min_n=int(1e9)
sum=0
for i in range(M,N+1):
    if isPrime(i):
        sum+=i
        min_n=min(min_n,i)
if sum==0 : print(-1)
else:
    print(sum)
    print(min_n)