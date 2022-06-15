''' [풀이]
각 도시 기준으로 생각
  - 해당 도시의 왼쪽 도시들 중 제일 주유 비용이 작은 값 확인
  - 해당 도시의 주유소 리터당 가격을 제일 작은 값으로 바꿈
  - 비용 += 길이 * 주유소의 리터당 가격
'''

import sys
input = sys.stdin.readline

# 도시의 개수를 나타내는 정수 N(2 ≤ N ≤ 100,000) 입력
N = int(input())

length = list(map(int, input().split())) # 인접한 두 도시를 연결하는 도로의 길이
price = list(map(int, input().split())) # 주유소 리터당 가격

min_price = price[0]

# 최소 비용 저장
ans = price[0]*length[0]

# 각 도시 기준으로 생각
for i in range(1, N-1):
  # 해당 도시의 왼쪽 도시들 중 제일 주유 비용이 작은 값 확인
  if min_price > price[i]:
    # 제일 작은 값으로 비용 바꿈
    min_price = price[i]

  # 비용 += 길이 * 주유소의 리터당 가격
  ans += length[i]*min_price
    
print(ans)


## ============= 부분점수 41점 코드 ============== ##
# import sys
# input = sys.stdin.readline

# # 도시의 개수를 나타내는 정수 N(2 ≤ N ≤ 100,000) 입력
# N = int(input())

# length = list(map(int, input().split())) # 인접한 두 도시를 연결하는 도로의 길이
# price = list(map(int, input().split())) # 주유소 리터당 가격

# # 최소 비용 저장
# min_price = price[0]*length[0]

# # 각 도시 기준으로 생각
# for i in range(1, N-1):
#   # 해당 도시의 왼쪽 도시들 중 제일 주유 비용이 작은 값 확인
#   if min(price[:i])<price[i]:
#     # 제일 작은 값으로 비용 바꿈
#     price[i]=min(price[:i])
    
#   # 비용 += 길이 * 주유소의 리터당 가격
#   min_price += length[i]*price[i]
    
# print(min_price)
## =========================================== ##