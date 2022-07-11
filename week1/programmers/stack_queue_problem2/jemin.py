from collections import deque


def solution(priorities, location):
    q = deque(enumerate(priorities))
    count = 0

    while q:
        m = q.index(max(q, key=lambda x: x[1]))
        for _ in range(m):
            q.append(q.popleft())

        i, _ = q.popleft()
        count += 1
        if i == location:
            return count
