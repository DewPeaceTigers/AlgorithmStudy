"""
곱이 최대인 경우는, 평균적으로 수들이 클 때 가장 큰 곱을 나타냄
"""

def solution(n, s):
    if n > s:
        return [-1]
    
    p, q = divmod(s, n)
    answer = [p] * n
    
    # 나머지 q: 뒤에서부터 q개 +1씩 더해줌
    for i in range(q):
        answer[n-1-i] += 1
        
    return answer