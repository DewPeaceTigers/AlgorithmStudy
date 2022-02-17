import sys
input = sys.stdin.readline
n=int(input())
lines=[]
for _ in range(n):
    lines.append(list(map(int,input().split())))
lines.sort()
draw=lines[0]
line_cnt=lines[0][1]-lines[0][0]
for x,y in lines[1:]:
    d_x,d_y=draw
    if d_x<= x <=d_y: # 이미 그려진 부분에 포함
        if not(d_x<= y <= d_y): # 포함 X
            line_cnt+= y-d_y
            draw[1]=y
    else: #if not isLined: # 길이는 쟀고, 정렬을 해두었기에 그 전 꺼는 더 이상 포함될 상황이 없다.
        draw=[x,y]
        line_cnt+=y-x
print(line_cnt)

## 스위핑
# 차근 차근 왼쪽에서 오른쪽으로 이동하면서 해결하는 방법
# 스캔하면서 쓸어간다.