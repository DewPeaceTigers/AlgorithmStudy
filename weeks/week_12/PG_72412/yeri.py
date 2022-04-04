"""효율성 박살"""
def solution(infos, queries):
    answer = []
    properties=[{"cpp":set(),"java":set(),"python":set()},{"backend":set(),"frontend":set()},{"junior":set(),"senior":set()},{"chicken":set(),"pizza":set()},[]]
    for i, info in enumerate(infos):
        info=info.split(" ")
        for j, inf in enumerate(info):
            if j == 4: properties[4].append(int(inf))
            else: properties[j][inf].add(i)
    for query in queries:
        query=query.split(" ")
        deserved=set([i for i in range(len(infos))])
        num=0
        for i,q in enumerate(query):
            if q =="and" or q=="-": continue
            elif i == len(query)-1:
                # 점수
                for cand in deserved:
                    if properties[4][cand]>=int(q): num+=1
            else:
                deserved = deserved.intersection(properties[i//2][q])
        answer.append(num)
    return answer
