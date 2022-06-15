import sys
input = sys.stdin.readline

# N (1 ≤ N ≤ 100,000) 입력
N = int(input())

# 이성 유형 
# - 키가 양수인 경우 : 키가 큰 여자
# - 키가 음수인 경우 : 키가 작은 여자

# 남자의 키 입력 (밀리미터 단위)
m_height = list(map(int, input().split()))
m_height.sort()

# 여자의 키 입력 (밀리미터 단위)
w_height = list(map(int, input().split()))
w_height.sort(reverse=True)

# print(m_height)
# print(w_height)

m_idx, w_idx =0, 0
ans=0

while m_idx<N and w_idx<N:
  # print(m_idx, w_idx, ans)
  if m_height[m_idx]*w_height[w_idx]<0: # 남자 키와 여자 키의 부호가 다른 경우
    if m_height[m_idx]<0: # 키가 음수
      # 키가 음수인 경우 : 키가 작은 여자
      if abs(m_height[m_idx])> w_height[w_idx]:
        ans+=1 # 한 쌍 증가
        m_idx+=1 # 다음 남자
    else: # 키가 양수
      # 키가 양수인 경우 : 키가 큰 여자
      if m_height[m_idx]<abs(w_height[w_idx]):
        ans+=1
        m_idx+=1 # 다음 남자
  w_idx+=1 # 다음 여자
  if w_idx<N and w_height[w_idx]<0: # 여자 키의 부호가 음수로 바뀌는 경우 처리
    while m_height[m_idx]<0: # 남자 키가 양수가 되는 인덱스 찾기
      m_idx+=1
      if m_idx>=N: # 인덱스가 N을 넘어가면 break
        break

print(ans)