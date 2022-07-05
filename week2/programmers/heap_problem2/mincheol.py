import heapq as hq


def solution(jobs):
    answer = 0
    N = len(jobs)
    jobs.sort()
    waiting = []
    current = jobs[0][0]
    total = 0
    check = 0
    while check < N:
        while jobs and jobs[0][0] <= current:
            job = hq.heappop(jobs)
            hq.heappush(waiting, [job[1], job[0]])

        if waiting:
            wait = hq.heappop(waiting)
            current = current + wait[0]
            total += current - wait[1]
            check += 1
        else:
            current += 1

    answer = total / N

    return int(answer)
