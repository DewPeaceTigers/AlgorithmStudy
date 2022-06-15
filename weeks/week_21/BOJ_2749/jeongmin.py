"""
풀이 찾아봄.. 피사노의 주기
- 피보나치 수를 어떤 수 K로 나눌 때, 나머지는 항상 주기를 가지게 된다.
- 주기의 길이를 P라고 하면 N번째 피보나치 수를 M으로 나눈 나머지는
    N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.
- M = 10^k 일 때 k>2라면, 주기는 항상 15 * 10^(k-1) 이다
"""

# n은 1,000,000,000,000,000,000보다 작거나 같은 자연수
n = int(input())

# 피사노 주기
p = 15 * (10 ** 5)

x1, x2 = 0, 1
for i in range(n%p-1):
    x1, x2 = x2, (x1+x2)%1000000

print(x2)