# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값
"""
문제 제대로 읽기!
- 구명보트는 작아서 '한 번에 최대 2명씩' 밖에 탈 수 없고, 무게 제한도 있습니다.
"""

def solution(people, limit):
    
    answer = 0
    
    people.sort(reverse = True)
    
    N = len(people)
    s = N-1
    
    for i in range(N):
        if i==s:
            answer += 1
            break
        elif i>s:
            break
        else:
            # 두 사람의 몸무게 합이 limit 보다 같거나 작으면
            if people[i]+people[s]<=limit:
                s-=1
            # 구명보트 한 개 추가
            answer+=1
    
    return answer