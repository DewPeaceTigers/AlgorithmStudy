import sys
input = sys.stdin.readline

N,C=map(int,input().split())
M = int(input())
boxes=[list(map(int,input().split())) for _ in range(M)]
#boxes.sort(key=lambda x:(x[1]))
boxes.sort()
print(boxes)
truck_pos=0
truck_pkg=[0]*(N+1) # 마을만큼 용량 만들어두기, 1부터 시작이라 한 칸 더 만들기
checked=0
done=0
for truck_pos in range(N):
    print(truck_pos)
    if truck_pkg[truck_pos+1]!=0: # 배송 물건 down
        print(truck_pos+1,"에서 내립니다..",end=" ")
        print(truck_pkg[truck_pos+1])
        done+=truck_pkg[truck_pos+1]
        truck_pkg[truck_pos+1]=0
    while True: # 배송 물건 up
        if checked==M or boxes[checked][0]!=truck_pos+1: break
        print(checked,"번에",truck_pos,"의 물건 올립니다..",end=" ")
        up,down,weight=boxes[checked]
        if sum(truck_pkg)+weight <= C: # 용량이 충분하다면
            truck_pkg[down]+=weight
            print(weight)
        else: # 용량 초과라면
            tmp = C-sum(truck_pkg)
            if tmp>0:
                truck_pkg[down]+= tmp
                print("exceed split",tmp)
            else:
                print("exceed failed",tmp)
        checked+=1
    print(truck_pkg)
print(done)