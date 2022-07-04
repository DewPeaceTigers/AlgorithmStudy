def solution(dirs):
    answer = 0
    dir_dict={'U' : [0, 1], 'L':[-1, 0], 'R':[1, 0], 'D':[0, -1]}
    cur_x, cur_y=0, 0
    visited=set()
    for dir in dirs:
        next_x, next_y = cur_x+dir_dict[dir][0], cur_y+dir_dict[dir][1]
        if -5<=next_x<=5 and -5<=next_y<=5 :
            visited.add((cur_x, cur_y, next_x, next_y))
            visited.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y=next_x, next_y
            
            
    return len(visited)//2