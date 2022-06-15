''' [풀이]
1. 두 수의 약수 각각 구하고 (d1, d2 리스트에 저장)
2. 최대 공약수, 최소 공배수 구하기
  - 최대 공약수: d1, d2 리스트에 공통으로 있는 값 중 최대값
  - 최소 공배수: ( n1 * n2 ) // 최대 공약수
'''

# 두 수 입력
n1, n2 = map(int, input().split())

d1=[1]
d2=[1]

# n1 약수 구하기
for i in range(2, n1//2+1):
  if n1%i==0:
    d1.append(i)
d1.append(n1)

# n2 약수 구하기
for i in range(2, n2//2+1):
  if n2%i==0:
    d2.append(i)
d2.append(n2)

gcd = 1 # 최대공약수
lcm = 1 # 최소공배수

# 최대 공약수 구하기
for d in d1:
  if d in d2:
    gcd = d

# 최소 공배수 구하기
lcm = gcd * (n1//gcd) * (n2//gcd)

print(gcd)
print(lcm)