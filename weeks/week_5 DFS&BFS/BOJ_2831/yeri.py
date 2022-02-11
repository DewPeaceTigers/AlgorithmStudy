# import sys
# input = sys.stdin.readline

# N=int(input())
# men = list(map(int,input().split()))
# women = list(map(int,input().split()))

# men.sort(key=lambda x:(abs(x),x))
# women.sort(key=lambda x:(abs(x),x))

# front,back=-1,N
# cnt=0

# res=[]
# for man in men:
#     if man<0:
#         while front<N:
#             front+=1
#             if women[front]>0 :
#                 if -man > women[front]:
#                     women[front]=0
#                     cnt+=1
#                 break

#     else:
#         while back>-1:
#             back -= 1
#             if women[back] < 0:
#                 if man < -women[back]:
#                     print('in')
#                     women[back]=0
#                     cnt += 1
#                 break
# print(cnt)

import sys
def conditionalCounter(boysOrGirlsPostive,girlsOrBoysnegative):
    postive=boysOrGirlsPostive
    negative=girlsOrBoysnegative
    def counter():
        count=0
        while postive and negative:
            if postive[-1]+negative[-1]<0:
                count+=1
                postive.pop()
                negative.pop()
            else:
                postive.pop()
        return count
    return counter
    
if __name__ == "__main__":
    input()

    boys=list(map(int,sys.stdin.readline().rstrip().split()))
    girls=list(map(int,sys.stdin.readline().rstrip().split()))

    boysPostive=sorted([i for i in boys if i>0])
    boysNegative=sorted([i for i in boys if i<0],reverse=True)
    girlsPostive=sorted([i for i in girls if i>0])
    girlsNegative=sorted([i for i in girls if i<0],reverse=True)

    bpgn=conditionalCounter(boysPostive,girlsNegative)
    gpbn=conditionalCounter(girlsPostive,boysNegative)

    print(bpgn()+gpbn())