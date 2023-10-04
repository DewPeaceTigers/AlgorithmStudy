# import heapq

# def solution(number, k):
#     heap = []
#     answer = ""
#     for n in number:
#         if len(heap)>=len(number)-k:
#             d = heapq.heappop(heap)
#             i = answer.index(d)
#             answer = answer[:i]+answer[i+1:]
#         heapq.heappush(heap,n)
#         answer+=n
#     return answer

def solution(number, k):
    answer = [] 
    
    for num in number:
        while answer and k>0 and answer[-1]< num: # 현재 숫자가 마지막 숫자보다 클 경우 마지막 숫자 빼기
            answer.pop()
            k-=1
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer # K개를 다 빼지 않았을 경우 나머지 K를 빼기 위함
    return ''.join(answer)