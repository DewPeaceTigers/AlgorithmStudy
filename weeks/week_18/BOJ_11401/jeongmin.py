"""풀이 찾아봄..
[페르마의 소정리]
- 한 마디로 임의의 소수 p와 서로소인 한 수의(p - 1)승을 p 로 나눈 나머지는 무조건 1이라는 정리입니다.
- 예를 들면 64^70을 71로 나눈 나머지는 1이라는 것을 순식간에 알 수 있습니다.

페르마의 소정리를 이용해서 분수를 정수로 바꿔줄 수 있음.
"""

# 페르마의 소정리 이용

# 분할 정복을 이용하여 a^b를 구한다.
def power(a, b):
    if b == 0:
        return 1

    x = power(a, b//2)

    if b % 2:  # 홀수이면
        return (x ** 2 * a) % p
    else:
        return (x ** 2) % p


p = 1000000007
N, K = map(int, input().split())

# nCk를 나타내기 위해 팩토리얼을 dp로 구해줍니다.
fact = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % p

# A는 nCk의 분자가되고 B는 분모가 됩니다.
A = fact[N]
B = (fact[N - K] * fact[K]) % p

#여기서 페르마의 소정리가 사용됨
print((A % p) * (power(B, p - 2) % p) % p)