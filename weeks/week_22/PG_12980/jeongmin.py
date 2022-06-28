def solution(n):
    
    usage = 1
    while n!= 1:
        # 홀수이면 한칸 이동
        if n%2 == 1:
            usage += 1
            n -= 1
        # 짝수이면 순간 이동
        else:
            n//=2
    
    ans = usage
    
    return ans

"""
# 다른사람 풀이
def solution(n):
    answer = 1
    while n > 1:
        answer += n % 2
        n = n // 2
    return answer
"""