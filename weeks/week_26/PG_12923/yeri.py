import math

def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        if i == 1: 
            answer.append(0)
        else:
            # 소수인지 아닌지 확인
            for j in range(2, int(math.sqrt(i)) + 1):
                mok = i // j
                if mok > 10 ** 7: # 최대 블록을 넘어가면 안됨
                    continue
                if i % j == 0:
                    answer.append(mok)
                    break
            else:
                answer.append(1)

    return answer