import math

def solution(progresses, speeds):
    answer = []
    date = []
    stack = []
    for i, prog in enumerate(progresses):
        date.append(math.ceil((100-prog)/speeds[i]))
    stack.append(date[0])
    compare = date[0]
    count = 1
    for i in range(1, len(date)+1):
        if i ==len(date):
            answer.append(count)
        elif compare < date[i]:
            compare = date[i]
            answer.append(count)
            count = 1
        else:
            count +=1
        
    return answer