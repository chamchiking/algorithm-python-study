def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        prev = len(phone_book[i-1])  # 바로 앞의 숫자
        if phone_book[i-1][0:prev] == phone_book[i][0:prev]:
            return False
    return True