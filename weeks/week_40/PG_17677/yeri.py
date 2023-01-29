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