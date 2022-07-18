n,m=map(int, input().split())
books=list(map(int, input().split()))

left=[]
right=[]
max_value=0
for book in books:
    if book>0:
        right.append(book)
    else:
        left.append(book)
    if abs(book)>abs(max_value) :
        max_value=book

right.sort(reverse=True)
left.sort()

lst=[]
for i in range(0, len(right), m):
  if right[i]!=max_value:
    lst.append(right[i])
    
for i in range(0, len(left), m):
  if left[i]!=max_value:
    lst.append(left[i])

result=abs(max_value)
for i in lst:
  result+=abs(i*2)
print(result)