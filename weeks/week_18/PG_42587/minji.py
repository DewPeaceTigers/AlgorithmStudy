def solution(priorities, location):
    answer = 0
    array=priorities
    count = 0
    i=0
    while count <= len(priorities) :
        for j in range(i+1, len(priorities)) :
            #print(priorities[i], priorities[j])
            if priorities[i]<priorities[j] :
                priorities.append(priorities.pop(i))
                i=0
                #print(priorities)
                if location == 0 :
                    location = len(priorities)-1
                else :
                    location-=1
        count+=1
        #print(count, location)
    answer=location+1
    return answer