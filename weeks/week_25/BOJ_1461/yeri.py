import sys
input = sys.stdin.readline
n,m = map(int,input().split())
books = list(map(int,input().split()))
books.sort()

pos = sorted([ book  for book in books if book>0 ],reverse=True)

neg = books[:len(books)-len(pos)]

dist = 0
for i in range(0,len(neg),m):
    dist += -neg[i]
for i in range(0,len(pos),m):
    dist += pos[i]
dist*=2
print(dist-abs(max(books,key=lambda x:abs(x))))