# 내 코드
import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
origins=list(map(int,input().split()))
temps=sorted(set(origins))
nums={}
for t in range(len(set(origins))): # 인덱스 딕셔너리로 저장
    nums[temps[t]]=t
res=[]
for origin in origins:
    res.append(nums[origin]) # 그 인덱스 찾아 출력
print(*res)

## 남의 코드
# import sys
# input=sys.stdin.readline
# print=sys.stdout.write

# N=int(input())
# arr=list(map(int,input().split()))
# sort_arr=sorted(set(arr))
# arr_dict={i:v for v,i in enumerate(sort_arr)}
# for i in arr:
#     print(f'{arr_dict[i]} ')