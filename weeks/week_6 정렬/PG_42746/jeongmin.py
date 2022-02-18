'''[풀이] 못 푼 문제.. 결국 답 찾아봄!
*3을 해주어 숫자들을 3번씩 반복해서 아스키값 순으로 정렬될 수 있도록 해주면 된다.
numbers 원소의 길이를 아래와 같이 제한해주었기 때문 (numbers의 원소는 0 이상 1,000 이하입니다.)
'''

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))