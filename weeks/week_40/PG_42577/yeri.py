def solution(phone_book):
    answer = True
    # phone_book.sort(key= lambda x:len(x))
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]: return False
            else: break
    return True