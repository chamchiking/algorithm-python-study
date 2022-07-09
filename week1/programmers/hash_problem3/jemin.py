def solution(clothes):
    from collections import Counter
    a = Counter(c[1] for c in clothes)
    print(a)
    c = list(Counter(c[1] for c in clothes).values())
    print(c)
    mul = 1
    for i in c:
        mul *= (i + 1)

    return mul - 1


def hash_solution(clothes):
    clothes_type = {}

    for _, type in clothes:
        if type not in clothes_type:
            clothes_type[type] = 1
        else:
            clothes_type[type] += 1
    cnt = 1
    for num in clothes_type.values():
        cnt *= (num + 1)

    return cnt - 1


def reduce_solution(clothes):
    from collections import Counter
    from functools import reduce

    cnt = Counter([kind for _, kind in clothes])
    return reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
