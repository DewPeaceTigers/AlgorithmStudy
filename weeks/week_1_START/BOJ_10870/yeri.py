N= int(input())
res=[]
for i in range(N+1):
    if i==0 or i==1 : res.append(i)
    else: res.append(res[i-1]+res[i-2])
print(res[-1])