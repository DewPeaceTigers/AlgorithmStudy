import re
def solution(files):
    head = re.compile('[\D]+')
    number = re.compile('[0-9]+')
    files_list=[]
    for file in files:
        h = head.findall(file)
        n = number.findall(file)
        files_list.append([h[0].lower(),int(n[0]),file])
    files_list.sort(key= lambda x:(x[0],x[1]))
    return [ file[-1] for file in files_list]