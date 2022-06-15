"""
풀이 찾아봄.. 중복 순열을 이용!
"""

from itertools import product

def solution(word):
    answer = 0

    words = ['A', 'E', 'I', 'O', 'U']

    dict_list = []

    for i in range(1, 6):
        dict_list += list(map("".join, product(words, repeat = i)))
    
    dict_list.sort()

    for i in range(len(dict_list)):
        if dict_list[i] == word:
            answer = i + 1
    
    return answer