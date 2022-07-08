def solution(prices):
    answer = []
    # 1. 끝까지 떨어지지 않는 경우
    for i in range(len(prices)-1):
        time = len(prices)-i-1
        # 2. 중간에 떨어지는 경우
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:  # 가격 떨어짐
                time = j-i
                break
        answer.append(time)
    answer.append(0)
    return answer