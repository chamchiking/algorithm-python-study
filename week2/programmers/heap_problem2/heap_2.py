import heapq

def solution(jobs):
    jobs.sort() # 요청시간을 기준으로 오름차순 정렬
    answer,now,i = 0,0,0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            # 요청시점이 현재시점 이전이라고 하면 
            if start < j[0] <= now:
                # heap에 종료시간, 요청시간 push (저장)
                heapq.heappush(heap, [j[1], j[0]])
        if heap:
            top = heapq.heappop(heap) # 종료시간
            start = now
            now += top[0] # 현재 시간 + 종료시간 = 현재 시간
            answer += (now - top[1]) 
            i += 1
        else:
            now += 1  
    return int(answer / len(jobs))