import sys
input = sys.stdin.readline

n,m = map(int,input().split())
r,c,d=map(int,input().split())
boxes=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,0,+1,0]
dy=[0,+1,0,-1]
cnt=0
while True:
    cnt+=1
    print(r,c,d,boxes[r][c])
    boxes[r][c]=2 # 청소함의 표시
    spin=0
    while spin!=4:
        d=(d+3)%4
        print(d)
        nr=r+dx[d]; nc=c+dy[d];
        if boxes[nr][nc]==0:
            r=nr; c=nc;
            break
        spin+=1
        if spin==4:
            print('four',spin)
            back=(d+2)%4
            print(d,'back',back)
            br= r+dx[back]; bc=c+dy[back]
            if boxes[br][bc]!=1:
                r=br; c=bc;
                spin=0
            else: break
    if spin==4:break
print(cnt)


