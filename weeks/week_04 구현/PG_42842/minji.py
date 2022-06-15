'''
brown+yellow는 카펫의 너비
=> brown+yellow=w*h

brown은 1줄로 된 테두리 이므로
카펫 가로 길이x2+(카펫 세로 길이-2)x2이다.
-> brown=2w+(h-2)*2
w+h=(brown+4)/2이다.
w=(brown+4)/2-h

공식을 정리하면
w((brwon+4)/2-w)=brown+yellow
2차 방정식이 나온다.
이것을 이용해서 카펫의 가로 길이와 세로 길이를 찾는다.
'''
import math


def solution(brown, yellow):
    answer = []

    S = brown + yellow  # 카펫 너비
    b = (brown + 4) / 2
    w, h = 0, 0  # 카펫의 가로 길이와 세로 길이
    # 근의 공식이용 b가 양수이므로 첫번째 해가 더 큼
    answer.append(int((b + math.sqrt(b ** 2 - 4 * S)) / 2))
    answer.append(int((b - math.sqrt(b ** 2 - 4 * S)) / 2))
    return answer