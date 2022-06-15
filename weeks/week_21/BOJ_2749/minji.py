'''
피사노 주기
주기가 p일때 N번째 피보나치수를 M으로 나눈 나머지는 N%P와 동일
M=10^k일때 주기는 항상 15*10^(k-1)
n번째 피보나치 수를 나눈 나머지는
n%p => n%(15*100000)
'''
n=int(input())
mod=1000000
fibo=[0, 1]
n=n%(15*100000)
for i in range(n) :
    fibo[0], fibo[1]=fibo[1]%1000000, (fibo[0]+fibo[1])%1000000

print(fibo[0])