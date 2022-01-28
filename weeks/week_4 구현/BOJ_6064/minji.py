'''
x는 x, x+M, x+2M ... 번째 해
y는 y, y+N, y+2N ... 번째 해
둘의 공통을 찾으면 된다.
<M:N>이 되면 달력의 마지막 해 이므로 최소공배수까지 반복하면 된다
x에서 M씩 증가 시키고 이 값에서 y를 빼고 N으로 나누었을 때 나머지가 0이면 답
'''
n=int(input())
for i in range(n) :
    M, N, x, y= map(int, input().split())
    ans=-1
    while x<=M*N :
        if (x-y) % N==0:
            ans=x
            break
        x+=M
    print(ans)

