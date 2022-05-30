k=int(input())
size=1
while k>size:
    size*=2

print(size, end=' ')

n=0
while True:
    if k%size==0 :
        print(n)
        break
    else:
        size//=2
        n+=1