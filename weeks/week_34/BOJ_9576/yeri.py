import sys
input = sys.stdin.readline
T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    books = [0]*(N+1)
    needs = [[0,0]]
    cnt=0
    for i in range(1,M+1):
        a,b = map(int,input().split())
        needs.append([a,b])
    needs.sort(key=lambda x:(x[1],x[0]))
    for i in range(1,M+1):
        a,b = needs[i]
        isRent = False
        rented = []
        for bi in range(a,b+1):
            if books[bi]==0:
                books[bi]=i
                isRent = True
                break
            else:
                rented.append(bi)
        r = 0
        while not isRent and r<len(rented):
            bi = rented[r]
            idx = books[bi]
            a,b = needs[idx]
            for ni in range(bi+1,b+1):
                if books[ni]==0:
                    books[ni] = idx
                    isRent = True
                    books[bi] = i
                    break
            if not isRent: r+=1
            if isRent : break
        if isRent:
            cnt+=1
    print(cnt)