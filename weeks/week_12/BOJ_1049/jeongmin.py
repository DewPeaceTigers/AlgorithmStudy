import sys
input = sys.stdin.readline
import math

# 기타줄의 개수 N(100이하 자연수)과 기타줄 브랜드 개수 M(50이하 자연수) 입력
N, M = map(int, input().split())

# 패키지 가격, 낱개 가격의 최솟값 저장
pMin, sMin = 1000, 1000
for _ in range(M):
  package, single = map(int, input().split())
  pMin = min(pMin, package)
  sMin = min(sMin, single)

money =0
# 패키지 가격만 선택하는 경우
# 패키지 가격 * (N//6) < 낱개 가격 * N
if pMin * math.ceil(N/6) < sMin *N:
  money = pMin * math.ceil(N/6)
elif pMin < sMin * 6:
  money = pMin * (N//6) + sMin*(N%6)
else:
  money = sMin * N

print(money)