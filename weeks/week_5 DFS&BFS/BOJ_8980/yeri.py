# import sys
# input = sys.stdin.readline

# N,C=map(int,input().split())
# M = int(input())
# boxes=[list(map(int,input().split())) for _ in range(M)]
# #boxes.sort(key=lambda x:(x[1]))
# boxes.sort()
# print(boxes)
# truck_pos=0
# truck_pkg=[0]*(N+1) # 마을만큼 용량 만들어두기, 1부터 시작이라 한 칸 더 만들기
# checked=0
# done=0
# for truck_pos in range(N):
#     print(truck_pos)
#     if truck_pkg[truck_pos+1]!=0: # 배송 물건 down
#         print(truck_pos+1,"에서 내립니다..",end=" ")
#         print(truck_pkg[truck_pos+1])
#         done+=truck_pkg[truck_pos+1]
#         truck_pkg[truck_pos+1]=0
#     while True: # 배송 물건 up
#         if checked==M or boxes[checked][0]!=truck_pos+1: break
#         print(checked,"번에",truck_pos,"의 물건 올립니다..",end=" ")
#         up,down,weight=boxes[checked]
#         if sum(truck_pkg)+weight <= C: # 용량이 충분하다면
#             truck_pkg[down]+=weight
#             print(weight)
#         else: # 용량 초과라면
#             tmp = C-sum(truck_pkg)
#             if tmp>0:
#                 truck_pkg[down]+= tmp
#                 print("exceed split",tmp)
#             else:
#                 print("exceed failed",tmp)
#         checked+=1
#     print(truck_pkg)
# print(done)

import sys

if __name__ == "__main__":
    n, c = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    box = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]


    box.sort(key=lambda x:x[1])  # 도착 시간이 빠른 순서로 정렬

    answer = 0  # 최대 박스 수
    remain = [c] * (n + 1)  # 각 위치에 남은 공간

    for i in range(m):
        temp = c  # c개를 옮길 수 있다고 가정
        for j in range(box[i][0], box[i][1]):
            temp = min(temp, remain[j])
        temp = min(temp, box[i][2])
        for j in range(box[i][0], box[i][1]):
            remain[j] -= temp
        answer += temp

    print(answer)
