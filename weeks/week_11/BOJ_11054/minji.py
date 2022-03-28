import sys

G=int(input())
P=int(input())
gate=[]
count=0

parent=list(range(G+1))

def find(x) :
    if parent[x]!=x :
        parent[x]=find(parent[x])
        return parent[x]
    else:
        return x
def union(a, b):
    root1=find(a)
    root2=find(b)
    if root1<root2:
        parent[root2]=root1
    else:
        parent[root1]=root2

for i in range(P) :
    gate.append(int(sys.stdin.readline()))

for i in range(P):
    x=find(gate[i])

    if x==0 :
        break

    union(x, x-1)
    count+=1

print(count)