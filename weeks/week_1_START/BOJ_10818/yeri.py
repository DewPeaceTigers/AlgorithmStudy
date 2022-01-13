N= int(input())
nums=list(map(int,input().split()))
max=-1000000; min=1000000;
for n in nums:
    if max < n : max=n
    if min > n : min=n
print(min,max)