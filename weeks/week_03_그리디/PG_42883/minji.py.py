def solution(people, limit):
    answer = 0
    people.sort()
    i , j =0, len(people)-1 #i는 앞, j는 뒤부터
    while i<=j :
        if people[i] + people[j] <= limit : #구명보트 하나에 둘을 태울수 있는 경우
            i += 1 
            j -=1
        else : #제한 무게를 초과해서 무거운 사람 한명만 구명보트에 태움
            j -=1
        answer+=1
    return answer