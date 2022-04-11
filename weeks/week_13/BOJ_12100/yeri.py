# import sys
# from copy import deepcopy

# input = sys.stdin.readline

# N=int(input())
# box=[list(map(int,input().split())) for _ in range(N)]
# def move(k,box):
#     # box 반환
#     if k==0:
#         for i in range(N):
#             pointer=0
#             for j in range(1,N):
#                 if box[i][j]:
#                     tmp = box[i][j]
#                     box[i][j] = 0
#                     # 마지막 칸은 확인 안함
#                     if box[i][pointer]==0:
#                         # 1. 앞이 0일 경우 칸을 앞으로 당김
#                         box[i][pointer]=tmp
#                     elif box[i][pointer]==tmp:
#                         # 2. 같을 경우 합치기
#                         box[i][pointer]*=2
#                         pointer+=1
#                     else:
#                         # 3. 다를 경우
#                         pointer+=1
#                         box[i][pointer]=tmp
#     elif k==1:
#         for j in range(N):
#             pointer=0
#             for i in range(1,N):
#                 if box[i][j]:
#                     tmp = box[i][j]
#                     box[i][j] = 0
#                     # 마지막 칸은 확인 안함
#                     if box[pointer][j] == 0:
#                         # 1. 앞이 0일 경우 칸을 앞으로 당김
#                         box[pointer][j] = tmp
#                     elif box[pointer][j] ==tmp:
#                         # 2. 같을 경우 합치기
#                         box[pointer][j] *= 2
#                         pointer+=1
#                     else:
#                         # 3. 다른 경우
#                         pointer+=1
#                         box[pointer][j]=tmp

#     elif k==2:
#         for i in range(N):
#             pointer=N-1
#             for j in range(N-2,-1,-1):
#                 if box[i][j]:
#                     tmp = box[i][j]
#                     box[i][j] = 0
#                     # 마지막 칸은 확인 안함
#                     if box[i][pointer]==0:
#                         # 1. 앞이 0일 경우 칸을 앞으로 당김
#                         box[i][pointer]=tmp
#                     elif box[i][pointer]==tmp:
#                         # 2. 같을 경우 합치기
#                         box[i][pointer]*=2
#                         pointer-=1
#                     else:
#                         # 3. 다를 경우
#                         pointer-=1
#                         box[i][pointer]=tmp
#     elif k==3:
#         for j in range(N):
#             pointer=N-1
#             for i in range(N-2,-1,-1):
#                 if box[i][j]:
#                     tmp = box[i][j]
#                     box[i][j] = 0
#                     # 마지막 칸은 확인 안함
#                     if box[pointer][j] == 0:
#                         # 1. 앞이 0일 경우 칸을 앞으로 당김
#                         box[pointer][j] = tmp
#                     elif box[pointer][j] == tmp:
#                         # 2. 같을 경우 합치기
#                         box[pointer][j] *= 2
#                         pointer-=1
#                     else:
#                         # 3. 다를 경우
#                         pointer-=1
#                         box[pointer][j]=tmp

#     return box

# max_num=0
# def dfs(cnt,box):
#     global max_num
#     if cnt==5:
#         for b in box: print(b)
#         max_num=max(max_num,max([max(b) for b in box]))
#         print(max_num)
#     else:
#         for i in range(4):
#             dfs(cnt+1,move(i,deepcopy(box)))

# dfs(0,deepcopy(box))
# print(max_num)


import sys
from copy import deepcopy
input = sys.stdin.readline

# INPUT
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# UP
def up(board):
    for j in range(n):
        pointer = 0
        for i in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 포인터가 가리키는 수가 0일 때
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[pointer][j]  == tmp:
                    board[pointer][j] *= 2
                    pointer += 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    pointer += 1
                    board[pointer][j] = tmp
    return board

# DOWN
def down(board):
    for j in range(n):
        pointer = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                elif board[pointer][j]  == tmp:
                    board[pointer][j] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board

# LEFT
def left(board):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer]= tmp
    return board

# RIGHT
def right(board):
    for i in range(n):
        pointer = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board


# DFS
def dfs(board, cnt):
    if cnt == 5:
        # 2차원 배열 요소 중 가장 큰 값 반환
        return max(map(max, board))

    # 상, 하, 좌, 우로 움직여 리턴한 값들 중 가장 큰 값 반환
    # board를 꼭 deepcopy하여 함수를 거친 board값이 다음 함수에 들어가지 못하도록 해주어야 한다.
    return max(dfs(up(deepcopy(board)), cnt + 1), dfs(down(deepcopy(board)), cnt + 1), dfs(left(deepcopy(board)), cnt + 1), dfs(right(deepcopy(board)), cnt + 1))

print(dfs(board, 0))

