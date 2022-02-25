# import sys
# input = sys.stdin.readline

# n,m=map(int,input().split())
# x=sorted(list(map(int,input().split())))
# def check(bound):
#     rays=[]
#     ray=0
#     for i in range(n):
#         if ray+x[i] <= bound:
#             ray+=x[i]
#         else:
#             rays.append(ray)
#             ray=x[i]
#     rays.append(ray)
#     if len(rays)==m: return True
#     else: return False

# start,end =x[0],sum(x) #x[len(x)-1]
# while start+1<end:
#     mid = (start+end)//2
#     if check(mid):
#         end=mid
#     else:
#         start=mid
# print(start,end)

def count(li, m):
    t = cnt = 0
    for n in li:
        if t+n > m:
            cnt += 1
            t = n
        else:
            t += n
    return cnt+1 # 나눠진 ray 개수 세기

N, M = map(int, input().split())
li = list(map(int, input().split()))
s, e = max(li), sum(li) # 가장 큰 것과 모두의 합이어야 함
res = 0
while s <= e:
    m = (s+e)//2
    if count(li, m) <= M: # 나눠진 개수가 m보다 작거나 같으면
        res = m # 답 
        e = m-1 # ??
    else:
        s = m+1 # ??
print(res)

## 나와의 차이가 뭐지..