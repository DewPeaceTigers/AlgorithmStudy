# 못품
# 같이 공부함
# LIS 알고리즘을 이용해야 한다.
# https://chanhuiseok.github.io/posts/algo-49/#2352%EB%B2%88--%EB%B0%98%EB%8F%84%EC%B2%B4-%EC%84%A4%EA%B3%84---%EB%AC%B8%EC%A0%9C-%EC%A1%B0%EA%B1%B4%EA%B3%BC-%EC%84%A4%EB%AA%85

# 우리
# import sys
# input = sys.stdin.readline

# n = int(input())
# ports=list(map(int,input().split()))

# arr=[0]*n
# arr_idx= 0
# arr[0] = ports[0]
# ports_idx = 1
# def search(left,right,target):
#     while left<right:
#         mid=(left+right)//2
#         if arr[mid] < target:
#             left = mid + 1
#         else :
#             right = mid
#     return right

# while ports_idx<n:
#     if arr[arr_idx] < ports[ports_idx]:
#         arr[arr_idx+1]=ports[ports_idx]
#         arr_idx+=1
#     else:
#         idx=search(0,arr_idx,ports[ports_idx])
#         arr[idx]=ports[ports_idx]
#     ports_idx+=1

# print(arr_idx+1)

#1
from bisect import bisect
import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
dp = [s[0]]
for i in range(1, n):
    if s[i] > dp[-1]:
        dp.append(s[i])
    else:
        dp[bisect(dp, s[i])] = s[i]
print(len(dp))

#2
# https://0equal2.tistory.com/101