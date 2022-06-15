'''
남자 여자 모두 음수일 경우와 양수일 경우 나눠서 list 넣어둠
minus의 경우 내림차순 정렬
1. 키 작은 여자와 춤 추고 싶은 경우(남자->음수)
    조건 1. 여자는 키큰 남자를 원해야함(여자->양수)
    조건 2. 키가 작은 순으로 정렬된 여자 키 앞에서부터 확인
    조건 3. 자기보다 큰 여자가 나오면 반복문 종료
2. 키 큰 여자와 춤 추고 싶은 경우(남자->양수)
    조건 1. 여자는 키 작은 남자를 원해야함(여자->음수)
    조건2. 키가 작은 순으로 정렬되어있으므로 뒤에서 부터 확인
    조건3. 자기보다 작은 여자가 나오면 반복문 종료
'''
import sys

N=int(sys.stdin.readline())

men=list(map(int, sys.stdin.readline().split()))
women=list(map(int, sys.stdin.readline().split()))

#음수 양수 별로 남자 여자 구분
men_plus=sorted([i for i in men if i >0])
men_minus=sorted([i for i in men if i <0], reverse=True)
women_plus=sorted([i for i in women if i > 0])
women_minus=sorted([i for i in women if i <0 ], reverse=True)

answer=0
def count(plus, minus):
    global answer
    i, j= 0, 0
    while i < len(plus) :
        while j < len(minus) :
            if plus[i]<abs(minus[j]) :
                j+=1
                answer+=1
                break
            else :
                j+=1
        if j == len(minus) :
            break
        i+=1


count(men_plus, women_minus) #남자는 키 큰 여자, 여자는 키 작은 남자
count(women_plus, men_minus) #남자는 키 작은 여자, 여자는 키 큰 남자
print(answer)