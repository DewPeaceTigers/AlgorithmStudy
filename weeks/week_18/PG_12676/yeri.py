import math


def solution(str1, str2):
    s1 = make_2_word(str1)
    s2 = make_2_word(str2)
    print(s1,s2)
    if s1 == [] and s2 == []:
        return 65536

    s1_copy = s1.copy()
    s2_copy = s2.copy()

    # 교집합
    inter = []
    for i in s1:
        if i in s2_copy:
            inter.append(i)
            s1_copy.remove(i)
            s2_copy.remove(i)


    # 합집합
    union = inter + s1_copy + s2_copy


    answer = math.floor((len(inter) / len(union)) * 65536)
    return answer


def make_2_word(s):
    s = s.upper()
    a = []
    for i in range(len(s) - 1):
        if s[i:i + 2].isalpha():
            a.append(s[i:i + 2])
    return a