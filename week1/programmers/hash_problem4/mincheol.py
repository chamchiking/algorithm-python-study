def solution(genres, plays):
    answer = []
    dict = {}
    play_dict = {}
    for i, genre in enumerate(genres):
        if genre not in dict.keys():
            dict[genre] = 0
            play_dict[genre] = []
        dict[genre] += plays[i]
        play_dict[genre].append([-plays[i], i])
    
    sorted_genre = sorted(dict.items(),key= lambda x: x[1], reverse=True)
    for genre in sorted_genre:
        list = play_dict[genre[0]]
        list.sort(reverse=True)
        if len(list)>=2:
            answer.append(list.pop()[1])
            answer.append(list.pop()[1])
        elif len(list) ==1:
            answer.append(list.pop()[1])
    
    return answer