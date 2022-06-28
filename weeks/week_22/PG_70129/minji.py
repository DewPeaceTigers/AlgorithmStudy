def solution(s):
    answer = []
    zero_cnt=0 #삭제한 0 횟수
    count=0 #변환 횟수
    while(s!="1") :
        zero_cnt+=s.count('0') #0의 개수 
        s=s.replace("0", "") #0을 제거
        s=bin(len(s))[2:] #길이를 2진수 변환
        count+=1 #변환과정 count

    answer.append(count)
    answer.append(zero_cnt)
    return answer

print(solution("1111111"))