from collections import deque
def solution(bridge_length, weight, truck_weights):
    start = 0
    loc = 0
    total = 0
    list = deque()
    index = 0
    while index < len(truck_weights) or total !=0:
        if loc < bridge_length:
            loc +=1
        else:
            loc +=1
            total -= list[start]
            start +=1
        
        if index < len(truck_weights):
            if (total + truck_weights[index]) <= weight:
                list.append(truck_weights[index])
                total += truck_weights[index]
                index +=1
            else:
                list.append(0)
    return loc