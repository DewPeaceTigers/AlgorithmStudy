import sys

def pos(now):
    """
    1. ���̰� 1�� ���� ��ġ ����
    2. ���� ���� < ���� ����, ���� ��ġ�� ���� ������ ��ĵ (���� ���� ���� ��ġ)
    3. ���� ���� > ���� ����, ���� ��ġ�� ���� ���� ��ĵ (���� ���� ���� ��ġ)
    :param i:
    :return:
    """
    for j in range(1, n):
        if abs(now[j] - now[j - 1]) > 1:   # 1. ���̰� 1�� ����
            return False
        if now[j] < now[j - 1]:            # 2.  ���� < ����, ���θ� ����� ���� �������� ��ĵ��(���� ���� ���� ��ġ)
            for k in range(l):  # l ��ŭ ���� �ʺ� �ʿ� 
                if j + k >= n or used[j + k] or now[j] != now[j + k]: # ���� �Ѿ or �̹� ��ġ�� or ���� ���� ���̰� �ٸ� ���, �׸�  
                    return False
                if now[j] == now[j + k]:   # ���̰� ���� ��� ��� ���� üũ 
                    used[j + k] = True
        elif now[j] > now[j - 1]:         # 3.  ���� > ����, ���θ� ����� ���� ������ ��ĵ��
            for k in range(l):
                if j - k - 1 < 0 or now[j - 1] != now[j - k - 1] or used[j - k - 1]:  # ���� �Ѿ or �̹� ��ġ�� or ���� ���� ���̰� �ٸ� ���, �׸�
                    return False
                if now[j - 1] == now[j - k - 1]:   # ���̰� ���� ��� ��� ���� üũ 
                     used[j - k - 1] = True
    return True   # ��� �������� ��ġ�� ��� �������� ��� 
    
n, l = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0

# 1. ���� Ȯ��
for i in range(n):
    used = [False for _ in range(n)]  # ��� ����
    if pos(graph[i]):  # ���� Ȯ���� ���� �־��ش�.
        result += 1

# 2. ���� Ȯ��
for i in range(n):
    used = [False for _ in range(n)]
    if pos([graph[j][i] for j in range(n)]):  # ���� Ȯ���� ���� �־��ش�.
        result += 1