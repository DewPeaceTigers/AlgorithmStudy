'''
nCk를 구하면 됨
n!/(n-k)!k!

분수에는 mod 사용 불가능
(k!(n-k)!)^-1%1000000007
=(k!(n-k)!)^(1000000007-2)%1000000007
'''
n, k=map(int, input().split())
p=1000000007
def factorial(num) :
    n=1
    for i in range(2, num+1) :
        n=(n*i)%p

    return n


def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p

A=factorial(n)
B=(factorial(n-k)*factorial(k))%p

print(A * square(B, p-2) % p)

