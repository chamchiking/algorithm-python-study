import heapq

# 최소힙 - 각 요소를 그대로 저장
# D-1은 최소힙에서 pop 후 heapify
# D1은 최소힙에서 heappop

def solution(operations):
    answer = []
    
    q = []
    for op in operations:
        if op[0] == "I":
            # insert
            value = int(op[2:])
            heapq.heappush(q, int(value))
        elif op == "D 1":
            # delete max_value
            if len(q) > 0:
                heapq.heapify(q)
                value = q.pop()
        elif op == "D -1":
            # delete min_value
            if len(q) > 0:
                value = heapq.heappop(q)
    
    print(q)
    if len(q) > 0:
        answer = [max(q), min(q)]
    else:
        answer = [0, 0]
    return answer