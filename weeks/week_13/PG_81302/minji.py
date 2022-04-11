def solution(places):
    answer = []
    for place in places:
        check=True
        for i in range(5) :
            if check==False :
                break
            for j in range(5) :
                if check==False:
                    break
                if place[i][j]=='P' :
                    if i+1<5 and place[i+1][j]=='P' :
                        check=False
                        break
                    if i+2<5 and place[i+1][j]=='O' and place[i+2][j]=='P' :
                        check=False
                        break
                    if j+1<5 and place[i][j+1]=='P' :
                        check=False
                        break
                    if j+2<5 and place[i][j+1]=='O' and place[i][j+2]=='P' :
                        check=False
                        break
                    if i+1<5 and j+1<5 and place[i+1][j+1]=='P' and (place[i][j+1]=='O' or place[i+1][j]=='O') :
                        check=False
                        break
                    if i+1<5 and j-1>=0 and place[i+1][j-1]=='P' and (place[i][j-1]=='O' or place[i+1][j]=='O') :
                        check=False
                        break
        if check==False:
            answer.append(0)
        else :
            answer.append(1)
    return answer