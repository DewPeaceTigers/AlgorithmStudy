def getTime(start,end):
    sh,sm = map(int,start.split(":"))
    eh,em = map(int,end.split(":"))
    h = eh-sh
    m = em-sm
    return h*60+m
def getSheet(music):
    sheet=[]
    temp = ''
    for i in range(len(music)):
        if music[i]=="#":
            sheet.append(temp.lower())
            temp = ''
        elif temp=='':
            temp= music[i]
        else:
            sheet.append(temp)
            temp = music[i]
    if temp:
        sheet.append(temp)
    return sheet
def getRealSheet(sheet,time):
    length = len(sheet)
    real_sheet = []
    if time<length:
        real_sheet = sheet[:time]
    elif length == time:
        real_sheet = sheet
    else:
        for _ in range(time//length):
            real_sheet +=sheet
        if time%length!=0:
            left = time%length
            real_sheet+=sheet[:left]
    return real_sheet
def solution(m, musicinfos):
    answer = []
    for info in musicinfos:
        start, end, name, music = info.split(",")
        time = getTime(start,end)
        sheet = getSheet(music)
        mine = getSheet(m)
        real_sheet = getRealSheet(sheet,time)
        sheet_text = ''.join(real_sheet)
        mine_text = ''.join(mine) 
        if mine_text in sheet_text:
            answer.append((time,name))
    answer.sort(key=lambda x:-x[0])
    return answer[0][1] if answer else "(None)"