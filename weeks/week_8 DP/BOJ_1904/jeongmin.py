'''[풀이]
점화식 찾기!
tile[i] = tile[i-2] + tile[i-1]
  - tile[i-2]: 뒤에 00이 붙는 경우
  - tile[i-1]: 뒤에 1이 붙는 경우
'''

import sys
input= sys.stdin.readline

# N 입력(1 ≤ N ≤ 1,000,000)
N = int(input())

tile = [0] * (N+1)

tile[1]=1 # N=1일 때 초기화
if N>1: tile[2]=2 # N이 2이상인 경우 초기화

for i in range(3, N+1):
  tile[i]=(tile[i-2]+tile[i-1])%15746

print(tile[N])