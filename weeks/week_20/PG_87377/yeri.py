def findIntersection(line1,line2):
    a,b,c = line1
    d,e,f = line2
    if a*e == b*d:
        return []
    x = (b*f-c*e)/(a*e-b*d)
    y = (c*d-a*f)/(a*e-b*d)
    if x==int(x) and y==int(y):
        return [int(x),int(y)]
    else : return []
def solution(line):
    intersects=[]
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            intersect = findIntersection(line[i],line[j])
            if intersect:
                intersects.append(intersect)
    print(intersects)
    max_x = max(intersects,key= lambda x: x[0])[0]
    min_x = min(intersects,key= lambda x: x[0])[0]
    max_y = max(intersects,key= lambda x: x[1])[1]
    min_y = min(intersects,key= lambda x: x[1])[1]
    
    answer = ['.' * (max_x-min_x+1)] * (max_y-min_y+1)
    for x,y in intersects:
        answer[max_y-y] = answer[max_y-y][:x-min_x] + '*' + answer[max_y-y][x-min_x+1:]
    return answer