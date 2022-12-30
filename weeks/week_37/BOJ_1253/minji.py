n=int(input())

nums=list(map(int, input().split()))

nums.sort()
cnt=0
for i in range(n):
    temp=nums[:i]+nums[i+1:] #이거 왜 이렇게...?
    left, right=0, len(temp)-1
    while left<right:
        total=temp[left]+temp[right]
        if total==nums[i] :
            cnt+=1
            break
        if total<nums[i]:
            left+=1
        else:
            right-=1
print(cnt)