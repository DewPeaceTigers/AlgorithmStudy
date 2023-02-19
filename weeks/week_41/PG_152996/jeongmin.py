# 다른 사람 풀이 참고!
from collections import Counter

def solution(weights):
    answer = 0
    
    count = Counter(weights)
    
    # 무게가 같은 경우 처리
    for k, v in count.items():
        if v > 1: 
            # v개 중 2개를 뽑는 경우의 수
            answer += v * (v-1) / 2
    
    weights = list(set(weights))
    
    # 배율 3/4, 2/3, 1/2 확인!
    check = (3/4, 2/3, 1/2)
    
    for w in weights:
        for c in check:
            if w*c in weights:
                answer += count[w] * count[w*c]
    
    return answer

"""
[다른 사람 풀이 #2]
https://yejin72.tistory.com/109

1. 몸무게와 해당 몸무게를 가진 사람의 수을 키와 값으로 갖는 딕셔너리 사용
2. 한 사람의 몸무게가 w이라고 했을 때, 그 사람은 w, 2w, 1/2w, 2/3w, 3/2w, 4/3w, 3/4w의 몸무게를 지닌 사람들과 균형있게 시소를 탈 수 있다.
3. 쌍을 이룰 수 있는 사람들의 수를 모두 더한 뒤, 자신의 몸무게도 딕셔너리에 체크
""" 

# from collections import defaultdict

# def solution(weights):
#     answer = 0
#     info = defaultdict(int)
#     for w in weights:
#         answer += info[w] + info[w*2] + info[w/2] + info[(w*2)/3] + info[(w*3)/2] + info[(w*4)/3] + info[(w*3)/4]
#         info[w] += 1
#     return answer
