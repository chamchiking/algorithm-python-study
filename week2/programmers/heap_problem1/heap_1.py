import heapq
# 최대힙 사용: 부모노드의 값이 자식노드들의 값보다 항상 큰 힙

def solution(scoville, K):
    scoville.sort()
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        else:
            top = heapq.heappop(scoville) # 가장 작은 값
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, top+second*2)
            answer += 1
    return answer