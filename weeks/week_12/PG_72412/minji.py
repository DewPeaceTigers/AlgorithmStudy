'''
정확성만 통과
def solution(info, query):
    answer = []
    for q in query :
        q=q.replace("and ", "")
        q=q.split()
        count = 0
        for i in info :
            i=i.split()
            check=True
            if int(i[4])<int(q[4]):
                check=False
            else:
                for index in range(4) :
                    if q[index] =='-' :
                        continue
                    else:
                        if q[index]!=i[index] :
                            check=False
                            break
            if check :
                count+=1
        answer.append(count)
    return answer
'''
'''
info정보와 점수를 이용해서 하나의 info에서
경우의 수를 만듬.
'''
from collections import defaultdict
from itertools import combinations


def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_key = info[:-1]  # info정보
        info_value = int(info[-1])  # 점수
        for i in range(5):
            for c in combinations(info_key, i):  # 가능한 info 조합
                temp_key = ''.join(c)
                info_dict[temp_key].append(info_value)

    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3):  # and 제거
            query.remove('and')
        while '-' in query:  # -제거
            query.remove('-')
        temp_q = ''.join(query)

        if temp_q in info_dict:
            scores = info_dict[temp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while start < end:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)

    return answer