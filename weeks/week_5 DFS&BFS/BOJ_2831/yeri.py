import sys
input = sys.stdin.readline

N=int(input())
men = list(map(int,input().split()))
women = list(map(int,input().split()))

men.sort(key=lambda x:(abs(x),x))
women.sort(key=lambda x:(abs(x),x))

front,back=-1,N
cnt=0

res=[]
for man in men:
    if man<0:
        while front<N:
            front+=1
            if women[front]>0 :
                if -man > women[front]:
                    women[front]=0
                    cnt+=1
                break

    else:
        while back>-1:
            back -= 1
            if women[back] < 0:
                if man < -women[back]:
                    print('in')
                    women[back]=0
                    cnt += 1
                break
print(cnt)