def solution(numbers) :
    answer=''
    numbers=list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True) #���ڸ� 3�� �ݺ���Ű�� �� ���� ����
                   
    return str(int(''.join(numbers)))