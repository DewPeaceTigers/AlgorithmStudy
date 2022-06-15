T=int(input())
for _ in range(T):
    n=int(input())
    n = str(bin(n))
    for t in range(len(n)-1,-1,-1):
        if n[t]=='1': print(len(n)-t-1)