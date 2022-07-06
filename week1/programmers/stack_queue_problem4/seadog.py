# 매초를 증가시키며 초를 스택에 넣어두고 현재 시간의 가격과 스택 마지막 시간의 가격을 비교해서
# 스택에서 꺼낸 뒤 꺼낸 시간 - 넣었을 때의 시간을 떨어지지 않은 계산

def solution(prices):
    answer = []

    answer = [0 for _ in range(len(prices))]

    insert_time_stack = []
    for i in range(len(prices)):
        if len(insert_time_stack) > 0:            
            # 마지막 요소 비교 때 가격이 떨어짐. 몇개나 떨어졌을지 확인이 필요하므로 반복 필요
            while len(insert_time_stack) > 0 and prices[i] < prices[insert_time_stack[-1]]:
                t = insert_time_stack[-1]
                none_decrese_time = i - insert_time_stack.pop()
                answer[t] = none_decrese_time
        
        # 해당 초 기준으로 꺼내고 난 뒤에 넣기
        insert_time_stack.append(i)

    # 전부 다 돌고 나오지 못한 요소는 전체 시간 - 들어간 시간으로 버틴 시간 계산
    for i in range(len(insert_time_stack)):
        t = insert_time_stack[-1]
        none_decrese_time = len(prices) - insert_time_stack.pop() - 1
        answer[t] = none_decrese_time

    return answer