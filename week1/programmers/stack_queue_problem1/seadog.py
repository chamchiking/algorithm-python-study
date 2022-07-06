# 100이 돼서 배포가 가능한 최소 일수를 저장해서 순서대로 꺼내기

from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    
    q = deque()

    for i in range(len(progresses)):
        least_use_days = math.ceil((100 - progresses[i]) / speeds[i])
        q.append(least_use_days)

    print(q)
    base_days = q[0]
    count = 0
    while len(q) > 0:
        print(base_days)
        print(f"count is {count}")
        print(f"q len is {len(q)}")
        if q[0] > base_days:
            answer.append(count)
            base_days = q[0]
            count = 0
        else:
            q.popleft()
            count = count + 1
    
    if count > 0:
        answer.append(count)

    print(q)

    return answer