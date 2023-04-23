def solution(cards):
    answer = 0
    n = len(cards)
    for card in cards:
        check = [False] * (n + 1)
        G1 = 0
        open = card
        while 1:
            if check[open]:
                break
            else:
                G1 += 1
                check[open] = True
                open = cards[open - 1]
        if G1 == n:  # 상자를 다 열어버린 경우
            return 0
        tmp = []
        for card in cards:
            if not check[card]:
                tmp.append(card)

        for card in tmp:
            G2 = 0
            open = card
            while True:
                if check[open]:
                    answer = max(answer, G1 * G2)
                    break
                else:
                    G2 += 1
                    check[open] = True
                    open = cards[open - 1]

    return answer