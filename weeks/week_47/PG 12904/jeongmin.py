def solution(s):
    answer = 0

    N = len(s)
    # 모든 부분문자열 확인
    for i in range(N):
        for j in range(i+1, N+1):
          # 앞뒤를 뒤집어도 똑같은 경우
          if s[i:j] == s[i:j][::-1]:
            # 길이가 더 길면 업데이트
            if len(s[i:j]) > answer:
                answer = len(s[i:j])

    return answer