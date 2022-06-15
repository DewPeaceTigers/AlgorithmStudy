import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    p=list(input().strip())
    n=int(input())
    arr=input().strip().strip('[').strip(']').split(',')
    dir=1 # 정순
    index=0 # 현재 index
    front=0
    back=n-1
    end=back # 마지막 index
    popped=0
    for d in p:
        if d == 'R':
            dir=-dir
            if dir==1:
                back=index
                index=front
                end=back
            else:
                front=index
                index=back
                end=front
            #end= -1 if end==n else n
        elif d=='D':
            index+=dir
            popped+=1
    if popped>n:  #(dir==1 and index>end) or (dir==-1 and index<end):
        print('error')
    else:
        print('[',end='')
        for i in range(index,end+dir,dir):
            print(arr[i],end='')
            if i != end : print(',',end='')
        print(']')