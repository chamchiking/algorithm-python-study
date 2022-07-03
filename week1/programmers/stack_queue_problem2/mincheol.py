from collections import deque
def solution(priorities, location):
    q = deque([[p, i] for i, p in enumerate(priorities)])
    sort = []
    while q:
        current = q.popleft()
        count = False
        for ele in q:
            if ele[0] > current[0] and count==False:
                count = True
                break
                
        if count:
            q.append(current)
        else:
            sort.append(current)
    c = 1
    for s in sort:
        if s[1] ==location:
            return c
        c +=1