
def solution(numbers):
    answer = ''
    numbers2=[str(num)*3 for num in numbers] #문자 3번 반복한 값으로 변경
    numbers2 = list(enumerate(numbers2)) # 각 원소에 enumerate 함수로 인덱스 포함
    numbers2.sort(key=lambda x:x[1], reverse=True) #문자 기준 정렬 문자열로 변경하면 6 2 10 순서로 정렬됨

    for i, num in numbers2 :
        answer+=str(numbers[i])
    return str(int(answer))