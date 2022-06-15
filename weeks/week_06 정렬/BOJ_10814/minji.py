import sys

n=int(input())

people=[]
for i in range(n) : #입력
    age, name=map(str, sys.stdin.readline().split())
    age=int(age)
    people.append((age, name))

people.sort(key=lambda x:x[0])#나이순으로 정렬
for p in people :
    print(p[0], p[1])