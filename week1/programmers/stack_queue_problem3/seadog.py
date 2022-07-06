# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 시간 구하기

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    
    wait_q = deque() # 트럭 무게를 요소로 가짐
    crossing_q = deque() # [트럭 무게, 다리를 완전히 건너는 시간]을 요소로 가짐
    cur_weight = 0
    
    for truck_weight in truck_weights:
        wait_q.append(truck_weight)
        
    # 문제 조건 그대로 시뮬레이션
    while len(wait_q) > 0 or len(crossing_q) > 0:
        time = time + 1
        
        # 건너는 중인 트럭들 큐에서 가장 앞 요소의 나올 시간이 현재 시간보다 작다면
        if len(crossing_q) > 0 and crossing_q[0][1] <= time:
            truck_weight, out_time = crossing_q.popleft()
            cur_weight = cur_weight - truck_weight

        # 현재 다리 위의 무게 + 대기 중인 트럭 중 가장 앞 요소의 무게가 최대 하중 이하면
        if len(wait_q) > 0 and cur_weight + wait_q[0] <= weight:
            truck_weight = wait_q.popleft() # 대기 큐에서 꺼내기
            cur_weight = cur_weight + truck_weight # 현재 다리 위 하중에 무게 더하기
            crossing_q.append([truck_weight, time + bridge_length]) # 건너는 중 큐에 추가
        
    answer = time
    
    return answer