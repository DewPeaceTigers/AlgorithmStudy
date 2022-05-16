from math import floor

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_list.append(str2[i:i + 2])

    intersection_list = set(str1_list) & set(str2_list)
    union_list = set(str1_list) | set(str2_list)

    if len(union_list) == 0:
        return 65536

    intersection_len = sum([min(str1_list.count(intersection), str2_list.count(intersection)) for intersection in intersection_list])
    union_len = sum([max(str1_list.count(union), str2_list.count(union)) for union in union_list])

    answer = floor((intersection_len / union_len) * 65536)

    return answer