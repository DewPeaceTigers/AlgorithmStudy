def solution(phone_book):
    answer=True
    phone_book.sort()

    start=phone_book[0]
    for phone in phone_book[1:] :
        if phone.startswith(start) :
            answer=False
        else:
            start=phone
    return answer