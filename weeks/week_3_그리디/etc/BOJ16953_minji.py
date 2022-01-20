a, b = map(int, input().split())
count = 0

while b > a :
    if b % 2 == 0 :
        b = int(b/2)
        count+=1
    elif b%10 == 1 :
        b=int(b/10)
        count+=1
    else :
        break
if a==b :
    print(count+1)
else:
    print(-1)