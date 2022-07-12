# x를 n진법으로 변환
def tonum(x, n):
    num = ''
    while x>0:
        x, mod = divmod(x, n)
        if mod >= 10:
            num += chr(ord('A')+mod%10)
        else:
            num += str(mod)
    num = num[::-1]
    return num

def solution(n, t, m, p):
    answer = ''
    
    # game : 게임을 진행할 경우 말해야하는 숫자 순서
    i, game = 1, "0"
    while len(game)<m*t:
        game += tonum(i, n)
        i += 1
    
    # 튜브가 말해야 하는 숫자 구하기
    for i in range(p-1, m*t, m):
        answer += game[i]
    
    return answer