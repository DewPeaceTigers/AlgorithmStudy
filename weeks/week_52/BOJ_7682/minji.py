'''
최종 가능한 경우
1. 승자 없이 보드가 다 채워져있는경우
2. x개수-o개수가 0일때 o가 이긴경우
3. x개수-o개수가 1일때 x가 이긴경우
4. 보드가 다 채워져있는데 o가 이기지 않은 경우
'''
import sys

input=sys.stdin.readline

def check(boards, win) :
    if boards[0]==boards[1]==boards[2]==win:
        return True
    if boards[3]==boards[4]==boards[5]==win:
        return True
    if boards[6]==boards[7]==boards[8]==win:
        return True
    if boards[0]==boards[3]==boards[6]==win:
        return True
    if boards[1]==boards[4]==boards[7]==win:
        return True
    if boards[2]==boards[5]==boards[8]==win:
        return True
    if boards[0]==boards[4]==boards[8]==win:
        return True
    if boards[2]==boards[4]==boards[6]==win:
        return True
while True:
    s=input().rstrip()
    if s=='end' :
        break
    boards=list(map(str, s))
    x_count=boards.count('X')
    o_count=boards.count('O')
    #개수가 안맞는 경우
    if x_count-o_count>1 or x_count<o_count:
       print('invalid')
       continue
    x_win=check(boards, 'X')
    o_win=check(boards, 'O')
    if x_count==o_count and o_win:
        print('valid')
        continue
    if x_count==o_count+1 and x_win and not o_win:
        print('valid')
        continue
    if x_count==5 and o_count==4 and not o_win:
        print('valid')
        continue
    print('invalid')