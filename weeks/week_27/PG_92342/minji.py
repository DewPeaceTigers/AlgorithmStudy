from collections import deque

def bfs(n, info):    
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # �������� 1) ȭ�� �� �� ���
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # ���̾��� �̱��
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap  # �ִ������� ����
                    res.clear()
                res.append(arrow)  # �ִ��������� ���� ȭ���Ȳ ����
        
        elif sum(arrow) > n:  # �������� 2) ȭ�� �� �� ���
            continue
        
        elif focus == 10:  # �������� 3) ȭ�� �� �� ���
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        
        else:  # ȭ�� ���
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # ����ġ���� 1�� ���� ���
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0�� ���
    return res

def solution(n, info):
    winList = bfs(n, info)
    
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]