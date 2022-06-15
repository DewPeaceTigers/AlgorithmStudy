from itertools import product

def solution(word):
    answer = 0
    vowel = ['A', 'E', 'I', 'O', 'U']
    l = []
    for i in range(1, 6):
        l.extend(map(''.join, product(vowel, repeat=i)))
    l.sort()
    return l.index(word) + 1
    return answer