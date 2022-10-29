import sys
n, m=map(int, input().split())
books=list(map(int, input().split()))

plus=[]
minus=[]
max_book=0
for book in books :
    if book<0 :
        minus.append(book)
    else:
        plus.append(book)
    if abs(book)>max_book:
        max_book=abs(book)
plus.sort()
minus.sort()

ans=0
for i in range(len(plus)-1, -1, -m) :
    ans+=plus[i]*2
for i in range(0, len(minus), m) :
    ans+=abs(minus[i])*2

ans-=max_book
print(ans)