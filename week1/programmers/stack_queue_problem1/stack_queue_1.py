def solution(progresses, speeds):
    date = []
    for i in range(len(progresses)):
        temp1, temp2 = divmod(100-progresses[i], speeds[i])
        if temp2 > 0:
            temp1 += 1
        date.append(temp1)
    
    answer = []
    idx = 0
    for j in range(len(date)):
        if date[idx] < date[j]:
            answer.append(j-idx)
            idx = j
    answer.append(len(date) - idx)
    return answer