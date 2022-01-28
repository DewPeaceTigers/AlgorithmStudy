n=int(input())

count=0
num=666  #첫 시작 666
while True :
    if '666' in str(num) : #num에 666이 포함되어 있으면 count 1증가
        count+=1
    if count==n : #count와 n이 같으면 출력 후 반복 종료
        print(num)
        break
    num+=1