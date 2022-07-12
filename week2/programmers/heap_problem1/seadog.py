import heapq

def solution(scoville, K):
    answer = 0
    
    # scoville에서 가장 낮은 a 두번쨰로 낮은 b 꺼내기
    scoville_heap = scoville
    heapq.heapify(scoville_heap)
    
    count = 0
    while scoville_heap[0] < K:
        if len(scoville_heap) < 2:
            count = -1
            break

        min_s = heapq.heappop(scoville_heap)
        second_min_s = heapq.heappop(scoville_heap)

        new_food_s = min_s + (second_min_s * 2)
        heapq.heappush(scoville_heap, new_food_s)
        count = count + 1
    
    return count