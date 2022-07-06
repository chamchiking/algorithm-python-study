from collections import deque
import heapq

# 찾으려는 문서(location의 인덱스에 해당하는 요소)가 몇번째로 출력되는지
# 가장 앞에 있는 요소를 순서대로 꺼내기 위해 큐 사용
# 꺼낸 요소의 중요도가 가장 높은지를 판단하기 위해 heapq 사용

def solution(priorities, location):
    answer = 0
    
    q = deque() # [인덱스, 중요도]를 요소로 가질 q
    priority_q = [] # 중요도를 내림차순으로 저장할 heapq
    for i in range(len(priorities)):
        q.append([i, priorities[i]])
        heapq.heappush(priority_q,  - priorities[i])

    print_count = 0
    # 반복 전 미리 최고 중요도를 max_priority에 할당
    max_priority = heapq.heappop(priority_q)
    while True: # location의 문서를 출력할 때까지 시뮬레이션?
        i, priority = q.popleft()
        if priority == - max_priority: # 최고 중요도와 같다면
            print_count = print_count + 1
            if i == location: # 찾으려는 문서와 같다면
                break

            max_priority = heapq.heappop(priority_q)
        else: # 최고 중요도와 다르다면
            q.append([i, priority])


    answer = print_count

    return answer