import heapq
import math

# 구현
# 95점

def solution(jobs):
    answer = 0

    jobs = sorted(jobs)

    print(jobs)
    
    job_heapq = []
    
    work_time = 0
    cur_job_index = 0
    while True:
        if len(job_heapq) > 0:
            job = heapq.heappop(job_heapq)
            for i in range(len(jobs)): # 현재 시간 ~ 꺼낸 작업이 끝나는 시간까지 반복
                if work_time < jobs[i][0] <= work_time + job[0]: # 힙에 넣을 작업이 요청받은 시간이 현재시간보다 작다면 넣기
                    heapq.heappush(job_heapq, [jobs[i][1], jobs[i][0]]) # 소요시간, 힙에 들어온 시간
                    cur_job_index += 1
            print(work_time)
            print(job_heapq)
            work_time = work_time + job[0]
            answer = answer + (work_time - job[1]) / len(jobs)
        else:
            if cur_job_index < len(jobs) and work_time >= jobs[cur_job_index][0]:
                heapq.heappush(job_heapq, [jobs[cur_job_index][1], jobs[cur_job_index][0]]) # 소요시간, 힙에 들어온 시간
                cur_job_index += 1
            else:
                work_time += 1
            
        
        if work_time > 500000:
            break
        
    
    return int(answer)

# print(solution([[0, 3], [1, 9], [2, 6]]))
# print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))