import sys
import math

input = sys.stdin.readline

K = int(input())

# log2(K) 값 구하기
x = math.log2(K)

# K가 2의 제곱 형태이면
if x-int(x) == 0:
    size = 2**int(x)
    cnt = 0
else:
    size = 2**(int(x)+1)

    # 최소 몇번 쪼개야 하는지
    # K를 이진수로 변환, 하위비트에 연속으로 나오는 0 제거
    cnt = len(bin(K)[2:].rstrip("0"))
print(size, cnt)