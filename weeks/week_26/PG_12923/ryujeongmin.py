"""계속 시간초과... 풀이 찾아봄!"""

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        k = int(i != 1)  # i가 1이면 0, 1이 아니면 1을 대입
        for j in range(2, int(i**0.5)+1): # i**0.5 == sqrt(i)
            if i%j == 0 and i//j <= 10000000:
                k = i//j  # j가 2부터 커지기 때문에 처음 만나는 i//j가 약수 중 가장 큰 값
                break
        answer.append(k)
    
    return answer