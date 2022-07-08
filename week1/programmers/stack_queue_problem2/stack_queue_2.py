def solution(priorities, location):
    answer = 1
    index = list(range(len(priorities)))
    
    while priorities:
        top = priorities.pop(0)  # priorities 배열에서 1개씩 추출
        # 1개를 추출하고 나면 priorities는 top에 포함된거 빼고 담기게 됨
        i = index.pop(0)  # index(location) 배열에서 1개씩 추출
        
        if len(priorities) == 0:
            break
        
        if top < max(priorities): # 우선순위가 낮기 떄문에 뒤에 더해주는 경우
            priorities.append(top)
            index.append(i)
        elif i == location: # location 위치를 찾은 경우
            break
        else: # 우선순위가 높아서 인쇄하는 경우
            answer += 1
            
    return answer