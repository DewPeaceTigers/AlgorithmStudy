# ## 못품
# import sys
# input = sys.stdin.readline

# n,c=map(int,input().split())
# house=sorted([int(input()) for _ in range(n)])

# def check(bound):
#     cnt=1
#     idx=0
#     for i in range(n-1):
#         if house[i+1]-house[idx] >= bound:
#             cnt+=1
#             idx=i+1
#     return cnt

# start,end = 1, house[n-1]-house[0]
# res=0
# while start+1<end:
#      mid = (start+end)//2
#      cnt=check(mid)
#      if cnt >= c:
#          res=max(res,mid)
#          start=mid+1
#      else:
#          end=mid-1
# print(res)  