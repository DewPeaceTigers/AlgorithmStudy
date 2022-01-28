# 시간 초과.. 못품..
# t=int(input())

# for _ in range(t):
#     m,n,x,y=map(int,input().split())
#     i,j=1,1
#     cnt=1
#     while True:
#         if i==x and j==y: break
#         if i==m and j==n:
#             cnt=-1
#             break
#         # 다음 연도 구하기
#         if i==m: i=0
#         if j==n: j=0
#         i+=1; j+=1; cnt+=1
#     print(cnt)
# 시간 초과. 이렇게 하면 32억번 1을 더해줌..
# Q: (1씩 더해가면서 확인하는 코드) 왜 시간초과인가요?

# A: 답이 나와도 너무 오래 걸리면 안 됩니다. 여기에 있는 맨 처음 케이스에서 x와 y를 1씩 더하는 것만 세도 32억 번의 연산이 필요합니다. 
#힌트를 드리자면 일단 <x, y> 말고 x만 알맞은 값이 나오려면 몇 번째 해가 되어야 하는지 생각해 보세요.
# https://www.acmicpc.net/board/view/21503

t=int(input())

for _ in range(t):
    m,n,x,y=map(int,input().split())
    crit = x if x>y else y
    i,j= crit,crit # 첫 x가 나올 때는 j의 값도 x일 때이다.
    cnt=0 # 몇번의 m이 지났는지 : x를 기준으로 하는 것이기 때문에
    while True:  #cnt<40: #
        print(i,j)
        if i==x and j==y: break
        if i==crit and j==crit and cnt!=0:
            cnt=-1
            break
        if x>y:
            cnt+=1
            j= j+m-(n*((j+m)//n))
        else:
            cnt+=1
            i= i+n-(m*(i+n)//m)
    print(cnt*m+x if cnt!=-1 else -1) if x>y else print( cnt*n+y if cnt!=-1 else -1)