import sys

input=sys.stdin.readline

n, h=map(int, input().split())

up=[0]*(h+1)
down=[0]*(h+1)

for i in range(n) :
    if i%2==0:
        down[int(input())]+=1
    else:
        up[int(input())]+=1
        
for i in range(h-1, 0, -1) :
    up[i]+=up[i+1]
    down[i]+=down[i+1]
    
total=[0]*(h+1)
for i in range(1, h+1) :
    total[i]=down[i]+up[h-i+1]
 
total=total[1:]  
ans=min(total)
print(ans, total.count(ans))