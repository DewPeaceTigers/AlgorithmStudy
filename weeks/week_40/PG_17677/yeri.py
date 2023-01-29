def onlyNums(arr):
    newSet = set()
    for a in arr:
        if a.isalpha():
            newSet.add(a)
    return newSet

def make2wrdsList(arr):
    newArr=set()
    for i in range(len(arr)-1):
        newArr.add(arr[i]+arr[i+1])
    return newArr

def solution(str1,str2):
    if str1==str2=="" : return 65536
    set1 = onlyNums(make2wrdsList(list(str1.lower())))
    set2 = onlyNums(make2wrdsList(list(str2.lower())))
    comb = len(set1&set2)
    intersect = len(set1|set2)
    if intersect == 0 : return 65536
    return int(comb/intersect*65536)



##############

def div(str):
    res = []
    temp = str[0].lower()
    for i in range(1,len(str)):
        word = str[i].lower()
        if (temp+word).isalpha():
            res.append(temp+word)
        temp = word
    return res
def erase(str_list):
    res = []
    for str in str_list:
        if str.isalpha():
            res.append(str)
    return res
def solution(str1, str2):
    answer = 0
    list_1 = div(str1)
    list_2 = div(str2)
    same = []
    whole = []
    for word in list_1:
        if word in list_2:
            same.append(word)
            list_2.remove(word)
        whole.append(word)
    if list_2 : whole.extend(list_2)
    return 65536 if len(same)==0 and len(whole) == 0 else int(len(same)/len(whole)*65536)
