def solution(rows, columns, queries):
    answer = []
    boxes=[ [i*columns+j for j in range(1,columns+1)] for i in range(rows)]
    dx=[0,+1,0,-1]
    dy=[+1,0,-1,0]
    for start_x,start_y,end_x,end_y in queries:
        cur_x = start_x-1; cur_y = start_y-1;
        cur = boxes[cur_x][cur_y]
        dir=0
        changed=[]
        while dir<4:
            nx=cur_x+dx[dir]; ny = cur_y+dy[dir];
            if not(start_x-1<= nx <= end_x-1) or not(start_y-1<=ny<=end_y-1):
                dir= dir+1
                continue
            temp = boxes[nx][ny]
            boxes[nx][ny]=cur
            changed.append(cur)
            cur = temp
            cur_x=nx; cur_y= ny;
        answer.append(min(changed))
    return answer