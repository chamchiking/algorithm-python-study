def solution(bridge_length, weight, truck_weights):
    time = 0  # 다리를 건너는데 소요되는 시간
    passing_trucks = [0] * bridge_length  # 다리를 건너는 트럭 배열
    
    while passing_trucks:
        time += 1
        passing_trucks.pop(0)
        
        if truck_weights:
            if sum(passing_trucks) + truck_weights[0] <= weight:
                top = truck_weights.pop(0)
                passing_trucks.append(top)
            else:
                passing_trucks.append(0)
    
    return time