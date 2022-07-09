def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True


def hash_solution(phone_book):
    hash_map = {}
    for i in phone_book:
        hash_map[i] = 1
    for phone in phone_book:
        tmp = ''
        for s in phone:
            tmp += s
            if tmp in hash_map and tmp != phone:
                return False
    return True
