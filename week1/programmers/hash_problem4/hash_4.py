from collections import defaultdict

def solution(genres, plays):
    answer = []
    # genres_sum: 장르별 총 재생 횟수
    genres_sum = defaultdict(int)
    # music_plays: 장르별 [인덱스, 재생횟수]
    music_plays = defaultdict(list)
    
    for idx,[g,p] in enumerate(zip(genres, plays)):
        genres_sum[g] += p
        music_plays[g].append([idx, p])
    # genres_sum에 각 장르와 재생횟수 합 담김
    # music_plays에 각 장르에 속한 곡별 고유번호와 재생횟수 담김
    genres_sort = sorted(genres_sum.items(), key=lambda x:x[1], reverse=True)  
		# 내림차순으로 정렬해서 가장 많이 재생된 장르가 앞으로 오도록 (2개 추출)
    
    for key, val in genres_sort:
        # 재생횟수 기준으로 내림차순 정렬
        play_time = sorted(music_plays[key], key=lambda x:x[1], reverse=True)
        for idx, p in play_time[:2]:
            answer.append(idx)
    return answer