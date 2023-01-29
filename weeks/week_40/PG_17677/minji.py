import math

def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()

    str1_list=[]
    str2_list=[]

    #두즐가씩 끊어서 다중집합 원소
    for i in range(len(str1)-1) :
        str1_split=str1[i:i+2]
        if(str1_split.isalpha()) :
            str1_list.append(str1_split)
    for i in range(len(str2)-1) :
        str2_split=str2[i:i+2]
        if (str2_split.isalpha()):
            str2_list.append(str2_split)
    print(str1_list)
    print(str2_list)
    #합집합
    union=set(str1_list) | set(str2_list)
    #교집합
    intersection=set(str1_list) & set(str2_list)

    if(len(union)==0) :
        return 65536

    union_len=sum([max(str1_list.count(element), str2_list.count(element)) for element in union])
    intersection_len=sum([min(str1_list.count(element), str2_list.count(element)) for element in intersection])

    return math.floor((intersection_len/union_len)*65536)