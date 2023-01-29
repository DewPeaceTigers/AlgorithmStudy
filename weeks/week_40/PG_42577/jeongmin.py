def solution(phone_book):
    # 오름차순 정렬    
    phone_book.sort()
    
    # 번호 목록 저장
    phone = dict()
    for x in phone_book:
        for i in range(len(x)):    
            # 이전 번호 목록 중 해당 번호의 접두어인 경우가 있는지 확인
            if x[:i+1] in phone:
                return False
        # 번호 목록에 x번호 저장
        phone[x] = True
                
    return True
