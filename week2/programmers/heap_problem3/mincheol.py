import heapq as hq


def solution(operations):
    answer = []
    array = []
    total = 0
    for row in operations:
        split = row.split()
        op = split[0]
        num = int(split[1])
        if op == "I":
            array.append(num)
            array.sort()
            total += 1
        elif total > 0:
            if num == 1:
                array.pop()
                total -= 1
            else:
                array = array[1:]
                total -= 1

    if total == 0:
        answer = [0, 0]
    else:
        answer.append(array[-1])
        answer.append(array[0])
    return answer
