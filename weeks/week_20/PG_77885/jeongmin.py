"""풀이 찾아봄..."""

def solution(numbers):
    answer = []
    
    for number in numbers:
        # 짝수인 경우
        if number %2 ==0:
            # 마지막 0을 1로 변경 (+1)
            answer.append(number+1)            
        
        # 홀수인 경우
        else:
            # 2진수로 변환
            b= bin(number)
            b = b[:2]+"0"+b[2:]
            
            idx = 2     # 0이 나오는 인덱스 저장
            # 끝에서부터 0을 찾아서 0을 1로 바꿔줌
            # 0을 1로 바꾼 비트 다음 자리를 0으로 바꿈
            for i in range(len(b)-1, 1, -1):
                if b[i]=="0":
                    idx = i
                    break
            b = b[:idx]+"10"+b[idx+2:]
            
            # 2진수를 10진수로 변환 
            answer.append(int(b, 2))
    
    return answer