def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = array[commands[i][0]-1:commands[i][1]]#i번째부터 j번째까지 자름
        temp.sort()#정렬
        answer.append(temp[commands[i][2]-1]) #k번째 수
    return answer