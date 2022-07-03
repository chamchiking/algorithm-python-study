def solution(clothes):
    answer = 1
    counter = {}
    for cloth in clothes:
        if cloth[1] not in counter.keys():
            counter[cloth[1]] = 0
        counter[cloth[1]] +=1
    for i in counter.items():
        answer *= i[1]+1
    
    return answer-1