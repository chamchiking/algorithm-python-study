def solution(prices):
    size = len(prices)
    ans = []
    for i in range(size):
        for j in range(i+1, size):
            if prices[i] > prices[j]:
                ans.append(j - i)
                break
        else:
            ans.append(size - 1 - i)
    return ans
