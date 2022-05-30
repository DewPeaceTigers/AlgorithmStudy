'''
짝수는 맨 뒷자리가 1
홀수는 오른쪽부터 제일 처음 0이 나오는 자리가 1
'''
def solution(numbers):
    answer = []
    for number in numbers:
        if number%2==0 :
            answer.append(number+1)
        else:
            bin_num=list('0'+bin(number)[2:])
            for i in range(len(bin_num)-1, -1, -1) :
                if bin_num[i]=='0' :
                    bin_num[i]='1'
                    bin_num[i+1]='0'
                    break
            answer.append(int(''.join(bin_num), 2))
    return answer