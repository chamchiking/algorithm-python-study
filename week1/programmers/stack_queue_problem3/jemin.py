def solution(bridge_length, weight, truck_weights):
    q_moving = []
    trucks = truck_weights[:]
    time = 0
    while trucks:
        time += 1

        if q_moving and time - q_moving[0][1] == bridge_length:
            q_moving.pop(0)

        if weight >= sum(truck for truck, _ in q_moving) + trucks[0]:
            q_moving.append((trucks.pop(0), time))

    time += bridge_length
    return time


def q_solution(bridge_length, weight, truck_weights):
    q=[0] * bridge_length
    sec = 0
    while q:
        sec += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec
