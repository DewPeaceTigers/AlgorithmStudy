'''
T:테스트 케이스 수
N: A의 수, M:B의 수
A:A의 크기
B:B의 크기
'''
def binary_search(target,data):
    start=0
    end=len(data)-1
    ans=-1
    while start<=end :
        mid=(start+end)//2
        if data[mid]<target :
            ans=mid
            start=mid+1
        else:
            end=mid-1
    return ans
T=int(input())
for i in range(T) :
    N, M=map(int, input().split())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    A.sort()
    B.sort()
    count=0
    for a in A :
        count+=binary_search(a, B)+1
    print(count)

