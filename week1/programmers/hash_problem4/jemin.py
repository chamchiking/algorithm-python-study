def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for num, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic1:
            dic1[genre] = [(num, play)]
        else:
            dic1[genre].append((num, play))

        if genre not in dic2:
            dic2[genre] = play
        else:
            dic2[genre] += play

    for genre, _ in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for num, _ in sorted(dic1[genre], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(num)

    return answer
