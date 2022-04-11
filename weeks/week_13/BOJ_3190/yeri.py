N=int(input())
K=int(input())
apples=[]
for _ in range(K):
    apples.append(list(map(int,input().split())))
L=int(input())
directions=[]
for _ in range(L):
    x,c=input().split()
    directions.append((int(x),c))
snake=[[1,1]]
dir_i = 0
dir_y=[1,0,-1,0]
dir_x=[0,1,0,-1]
time=0
while(True):
    time+=1
    snake.insert(0,[snake[0][0]+dir_x[dir_i],snake[0][1]+dir_y[dir_i]]) # 한 칸 앞으로 몸 늘리기
    if snake[0][0]<1 or snake[0][0]>N or snake[0][1]<1 or snake[0][1]>N : break #벽과 부딪혔을 때 체크
    if snake[0] in snake[1:] : break #몸과 부딪혔을 때 체크

    if snake[0] in apples: # 움직인 위치에 사과가 있었다. -> 몸 유지
        del apples[apples.index(snake[0])]
    else: # 움직인 위치에 사과가 없었다. -> 꼬리 줄이기
        snake.pop()

    if directions and time == directions[0][0] : # 방향 지시가 남아있고, 정해진 시간 지났으니 방향 바꾸기
        if directions[0][1] =='L': dir_i= dir_i-1 if dir_i!=0 else 3
        elif directions[0][1] =='D': dir_i= dir_i+1 if dir_i!=3 else 0
        directions.pop(0)
print(time)