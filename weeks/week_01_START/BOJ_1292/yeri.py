A,B = map(int,input().split())
a,b=[0,0],[0,0]
res=0
for i in range(1,1001):
    res+=i
    if a[0]==0 and A<=res : a=[i,res if res!=1035 else 1000]
    if b[0]==0 and B<=res : b=[i,res-i]
    if a[0]!=0 and b[0]!=0 : break
sum=0
if a[0]==b[0]:
    sum= a[0]*(B-A+1)
else:
    for i in range(a[0],b[0]+1):
        if i == a[0] :
            sum+=a[0]*(a[1]-A+1)
        elif i == b[0]:
            sum+=b[0]*(B-b[1])
        else: sum+=i*i
print(sum)

# 1000까지 배열을 만들어서 하는 편이 낫다.