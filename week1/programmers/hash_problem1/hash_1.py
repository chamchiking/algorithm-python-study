from collections import Counter

def solution(participant, completion):
    answer = []
    full = participant + completion
    Count = Counter(full)
    for i in range(len(participant)):
				# Counter에서 완주하지 못한 사람은 등장횟수가 항상 홀수번임 (홀수에 해당되는 participant 찾아서 저장)
        if Count[participant[i]] % 2 == 0:
            pass
        else:
            answer.append(participant[i])
    return answer[0]