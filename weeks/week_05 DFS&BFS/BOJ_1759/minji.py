'''
조합을 이용해 문자 중에서 l개 만큼 조합을 list로 저장
첫번째 부터 하나씩 모음은 1개 이상 자음은 2개 이상인지 확인 후
조건에 만족하는 것만 출력
'''
import sys
import itertools

l, c=map(int, input().split())
ch=list(sys.stdin.readline().split())
ch.sort() #알파벳 순서 정렬
passwords=list(itertools.combinations(ch, l)) #암호 조합 저장
for password in passwords : #모음 1개 이상 자음 2개 이상 인지 확인
    vo = 0
    co = 0
    for i in range(l) :
        if password[i] in 'aeiou' : vo+=1  #모음인 경우
        else: co+=1 #자음 인 경우
    if vo>=1 and co>=2: #조건에 맞는 경우 출력
        print(''.join(password))
