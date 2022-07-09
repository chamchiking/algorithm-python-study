def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


def counter_solution(participant, completion):
    from collections import Counter

    result = Counter(participant) - Counter(completion)
    return list(result)[0]


def hash_solution(participant, completion):
    dict = {}
    sum = 0
    for i in participant:
        sum += hash(i)
        dict[hash(i)] = i
    for j in completion:
        sum -= hash(j)

    return dict[sum]
