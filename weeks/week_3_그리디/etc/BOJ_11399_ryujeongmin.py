''' [풀이]
돈을 인출하는데 걸리는 시간이 적은 순으로 정렬
각 사람[i]이 돈을 인출하는데 필요한 시간 = sum(p[:i+1])
'''

import sys
input = sys.stdin.readline

# 사람의 수 N(1 ≤ N ≤ 1,000) 입력
N = int(input())

# 각 사람이 돈을 인출하는데 걸리는 시간 Pi  (1 ≤ Pi ≤ 1,000) 입력
p = list(map(int, input().split()))
p.sort() # 오름차순 정렬

sum, ans=0, 0
for time in p:
  sum+=time
  ans+=sum
  # ans+=sum(p[:i+1]) # 위의 두 줄 한줄로 가능

print(ans)