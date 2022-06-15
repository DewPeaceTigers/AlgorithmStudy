''' [풀이]
1. people 내림차순 정렬
2. s라는 변수 추가 (디폴트값: n-1, 최솟값부터 시작)
3. 두 사람의 몸무게 합이 limit 보다 같거나 작으면 s -= 1
'''

def solution(people, limit):
    answer = 0
    
    n = len(people)
    s = n-1 # 최솟값부터 시작
    
    # 내림차순 정렬
    people.sort(reverse = True)
    for i in range(n):
        if i==s:
            # 구명보트 한 개 추가
            answer+=1
            break
        elif i>s:
            break
        else: # i<s 인 경우
            # 두 사람의 몸무게 합이 limit 보다 같거나 작으면
            if people[i]+people[s]<=limit:
                s-=1 # 위치 왼쪽으로 이동
            # 구명보트 한 개 추가
            answer+=1
            
    return answer