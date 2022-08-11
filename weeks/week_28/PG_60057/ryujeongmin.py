def solution(s):
    if len(s) == 1:
        return 1

    answer = 1000
    l = len(s) // 2 + 1

    # 문자를 자르는 단위: 1개~ (문자열길이//2)개
    for i in range(1, l):
        compression = ""    # 압축 문자열
        cnt = 1             # 반복 횟수
        unit = s[:i]

        for j in range(i, len(s), i):
            if unit == s[j:j + i]:
                cnt += 1
            else:
                if cnt > 1:
                    compression += str(cnt)
                compression += unit

                unit = s[j:j + i]
                cnt = 1

        if cnt > 1:
            compression += str(cnt)
        compression += unit

        answer = min(answer, len(compression))
    return answer