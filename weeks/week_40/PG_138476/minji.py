def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    sizes={}
    for size in tangerine :
        sizes[size]=sizes.get(size, 0)+1
    #개수가 많은 순으로 정렬
    sizes=sorted(sizes.values(), key=lambda x:-x)

    count=0
    for i in range(len(sizes)):
        count += sizes[i]
        if count>=k :
            return i+1
    return len(sizes)
