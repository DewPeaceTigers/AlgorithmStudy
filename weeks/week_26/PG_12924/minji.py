def solution(n):
    answer = 1 #n�� ��� 15=15
    for i in range(1, n+1) :
        sum=i
        for j in range(i+1, n+1) : #i���� ���ں��� �ϳ��� ������ ��
            sum+=j
            if sum==n : #n�� ������ +1
                answer+=1
                break
            elif sum>n : #n���� ũ�� ����
                break
            
    return answer