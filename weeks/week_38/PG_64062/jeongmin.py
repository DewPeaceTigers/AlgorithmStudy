"""
풀이 참고 -> https://school.programmers.co.kr/questions/41064
- O(n) 시간복잡도
- sliding window와 Deque 자료구조를 이용
"""

from collections import deque

def solution(stones, k):
    answer = 1e9
    
    # 디딤돌 개수
    N = len(stones)
    
    # i-k ~ i 번째 있는 디딤돌 숫자 저장
    q = deque()
    
    for i in range(N):
        # k개의 범위를 넘어가는 값 제거
        if q and q[0][0] <= i+1-k:
            q.popleft()
        
        # 큐에 있는 값이랑 뒤에서부터 비교해서 디딤돌 숫자가 더 큰 경우 
        while q and q[-1][1] < stones[i]:
            q.pop()
            
        q.append((i+1, stones[i]))
        
        if i+1>=k:
            answer = min(answer, q[0][1])
    
    return answer