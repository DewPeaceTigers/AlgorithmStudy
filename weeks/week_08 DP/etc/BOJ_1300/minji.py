#임의의 A보다 작거나 같은 수의 개수를 구하면 됨
#임의의 A/(행번호)=A보다 작거나 같은 수
#그 개수를 count하다보면 찾으려는 숫자를 알 수 있음
N=int(input())
K=int(input())

def binary_search(target, start, end) :
    while (start<=end):
        mid=(start+end)//2

        count=0
        for i in range(1, N+1) :
            count+=min(mid//i, N) #개수 count

        if count>=target :
            end=mid-1
        else:
            start=mid+1
    return start

print(binary_search(K, 1, N*N))