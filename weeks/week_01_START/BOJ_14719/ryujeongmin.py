''' [풀이]
1. 반복문 사용하여 왼쪽 열부터 차례로 확인
2. 열 기준 왼쪽 최댓값, 오른쪽 최댓값 구하기
3. 왼쪽, 오른쪽 최댓값 중 더 작은 값 (bound) 애 저장
4, 고이는 빗물 양 = (bound) - 블록 높이 

!틀렸던 이유!
예시를 만족하는 경우만 생각을 해서 로직을 잘못 짬
'''

# H, W 입력 (1 ≤ H, W ≤ 500)
H, W = map(int, input().split())

# 블록이 쌓인 높이 입력
blocks = list(map(int, input().split()))

# 고이는 빗물의 총량 저장
ans=0

# 왼쪽 열부터 차례로 확인 (양쪽 끝 제외)
for i in range(1, W-1):
    left_max = max(blocks[:i]) # 왼쪽 경계
    right_max = max(blocks[i:]) # 오른쪽 경계
    
    bound = min(left_max, right_max) # 왼쪽, 오른쪽 경계 중 최소
    
    if blocks[i]<bound:
        ans+= bound-blocks[i]

# 고이는 빗물의 총량 출력
print(ans)