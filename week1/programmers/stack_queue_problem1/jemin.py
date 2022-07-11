from math import ceil


def solution(progresses, speeds):
    # 시간 계산
    turns = [ceil((100 - a) / b) for a, b in zip(progresses, speeds)]

    ans = []
    idx = 0
    end = len(turns)
    for i in range(end):
        if turns[i] > turns[idx]:
            ans.append(i - idx)
            idx = i
    ans.append(end - idx)

    return ans
