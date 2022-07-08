import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for oper in operations:
        if oper[0] == 'I':
            heapq.heappush(min_heap, int(oper[1:]))
            heapq.heappush(max_heap, (-int(oper[1:]), int(oper[1:])))
        elif len(min_heap) == 0:
            continue
        elif int(oper[1:]) == -1:
            heapq.heappop(min_heap)
            max_heap.pop()
        else:
            heapq.heappop(max_heap)
            min_heap.pop()
    if len(min_heap) > 0:
        return [max_heap[0][1], min_heap[0]]
    else:
        return [0,0]