def solution(data):
    answer = []
    if len(data)==1:
        return 1
    for i in range(1,(len(data)//2)+1):
        right = data[:i]
        num = 1
        temp = ''
        for j in range(i,len(data),i):
            if right == data[j:j+i]: num+=1
            else:
                if num != 1:
                    temp+= str(num)+right
                else:
                    temp+=right
                right = data[j:j+i]
                num=1
        if num != 1:
            temp += str(num) + right
        else:
            temp += right
        answer.append(len(temp))
    return min(answer)