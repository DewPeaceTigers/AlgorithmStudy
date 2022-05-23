h, w, x, y=map(int, input().split())
B=[]
for _ in range(h+x):
    B.append(list(map(int, input().split())))

A=[[0]*(w+y) for _ in range(h+x)]

for i in range(h+x) :
    for j in range(w+y) :
        if x<=i<x+h and y<=j<y+w :
            A[i][j]=B[i][j]-A[i-x][j-y]
        elif i<x or i>=x+h:
            A[i][j]=B[i][j]
        elif j<y or j>=y+w :
            A[i][j]=B[i][j]

for i in range(h) :
    for j in range(w) :
        print(A[i][j], end=' ')
    print()
