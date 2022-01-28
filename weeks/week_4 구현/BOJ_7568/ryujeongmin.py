import sys
input = sys.stdin.readline

# 전체 사람의 수 N (2 ≤ N ≤ 50) 입력
N = int(input())

# 각 사람의 몸무게와 키 x,y 입력 (10 ≤ x, y ≤ 200)
people = [list(map(int, input().split())) for _ in range(N)]

# 등수 저장
rank =[1]*N

for i in range(N):
  for j in range(N):
    # 덩치가 더 큰 사람이 있는 경우
    if people[i][0]< people[j][0] and people[i][1]< people[j][1]:
      rank[i]+=1

print(*rank, sep=" ")
# for r in rank:
#   print(r, end=" ")