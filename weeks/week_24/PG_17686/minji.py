'''
정규 표현식 사용
[0-9] : 숫자 전체 의미
+:뒤에 숫자가 반복되어도 상관 x
() : 숫자를 기준으로 자름
'''
import re

def solution(files):
    answer = []
    temp=[]
    for file in files :
        temp.append(re.split(r"([0-9]+)", file)) #+는 반복 의미 숫자가 반복되도 됨
    
    sort_list=sorted(temp, key=lambda x:(x[0].lower(), int(x[1]))) #대문자 소문자 구분 x, 숫자부분은 int 형 정멸
    for s in sort_list:
        answer.append(''.join(s))
    
    return answer