from collections import deque
n = int(input())
card=deque([i for i in range(n)])
while len(card) > 1 :
    card.popleft()
    if len(card) == 1 :
        break
    card.append(card[0])
    card.popleft()
print(card[0]+1)