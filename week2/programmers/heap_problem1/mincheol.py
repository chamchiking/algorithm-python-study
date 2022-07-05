import heapq as h


def solution(scoville, K):
    answer = 0
    N = len(scoville)
    h.heapify(scoville)
    q1 = h.heappop(scoville)
    q2 = h.heappop(scoville)

    while q1 < K:
        h.heappush(scoville, q1 + (q2 * 2))
        answer += 1
        if len(scoville) >= 2:
            q1 = h.heappop(scoville)
            q2 = h.heappop(scoville)
        else:
            q1 = h.heappop(scoville)
            if q1 < K:
                answer = -1
                break

    return answer
