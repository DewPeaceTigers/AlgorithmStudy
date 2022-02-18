## 틀렸습니다.
# import sys
# input = sys.stdin.readline
# n=int(input())
# fluid=list(map(int,input().split()))
# fluid.sort(key=lambda x:abs(x))
# print(fluid)
# res=[]
# min_interval=int(1e9)
# min_friend=[]
# for i in range(n-1):
#     temp=abs(fluid[i]+fluid[i+1])
#     print(temp)
#     if min_interval > temp:
#         min_interval=temp
#         min_friend=[fluid[i],fluid[i+1]]
# print(*sorted(min_friend))

import sys
input = sys.stdin.readline
n=int(input())
fluid=list(map(int,input().split()))
fluid.sort()
print(fluid)
l,r=0,n-1
min_sum=2000000000
min_friends=[fluid[l],fluid[r]]
while l<r: # 이분 탐색 이용
    temp=fluid[l]+fluid[r]
    print(l,r,fluid[l]+fluid[r],temp)
    if min_sum > abs(temp):
        min_sum=abs(temp)
        min_friends=fluid[l],fluid[r]
    if temp <= 0: # 합친 값이 음수이면 0에 가까이 가기 위해서 더 큰 값을 더 해주는 것
        l+=1
    else: # 마찬가지로 합친 값이 양수이니깐 작은 값을 더해 0에 가까워지도록 하기
        r-=1
print(*min_friends)