import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    target = y - x

    result = 0

    # 이분탐색
    start, end = 0, 2**30
    while True:
        mid = (start + end) // 2

        # 범위 확인
        if (mid-1)**2 + (mid-1) < target <= mid**2:
            result = 2*mid - 1
            break
        elif mid ** 2 < target <= mid**2 + mid:
            result = 2*mid
            break

        elif target <= (mid-1)**2 + (mid-1):
            end = mid

        elif target > mid**2 + mid:
            start = mid

    print(result)

"""
(N칸) 1+2+...+x+(x-1)+...+2+1 : 요런 형태일 때 작동 횟수가 최솟값

이동 횟수가 i일 때 최대 이동 거리(D)
    1 => 1                      = 1
    2 => 1 + 1                  = 2
    3 => 1 + 2 + 1              = 4
    4 => 1 + 2 + 2 + 1          = 6
    5 => 1 + 2 + 3 + 2 + 1      = 9
    6 => 1 + 2 + 3 + 3 + 2 + 1 = 12
    ...

  위의 값을 일반화
  1. i = 2k-1(홀수) 일 때, 
     D = (1 + ... + (k-1))*2 + k 
       = k^2   
  
  2. i = 2k  (짝수) 일 때,
     D = (1 + ... + k)*2 
       = k^2 + k
       
target = y-x라 하면 아래 조건을 만족하는 k값을 구하면 된다!
  (k-1)**2 + (k-1) < target <= k**2         : 답 = 2k-1
        k**2       < target <= k**2 + k     : 답 = 2k
"""