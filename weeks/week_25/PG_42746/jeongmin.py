def solution(numbers):
    answer = ''
    
    info = []
    for i, number in enumerate(numbers):
        x = str(number)
        info.append(((x*4)[0:4], i))
    info.sort(reverse=True)
    
    for inf in info:
        answer += str(numbers[inf[1]])
        
    answer = str(int(answer))
    
    return answer


""" 다른 사람 풀이 """
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))