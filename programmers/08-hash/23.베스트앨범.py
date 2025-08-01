def solution(genres, plays):
    answer = []
    genres_dict = {}
    play_dict = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genres_dict:
            genres_dict[genre] = []
            play_dict[genre] = 0
        genres_dict[genre].append((i, play))
        play_dict[genre] += play

    # dict.items()는 key, value를 tuple 로 변환
    sorted_genres = sorted(play_dict.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_genres:
        # tuple의 정렬은 기본적으로 모든 값을 고려해줌
        # play에 음수를 취하고 오름차순 정렬함. 두 번째도 오름차순(id가 작은 게 먼저)가 됨
        sorted_songs = sorted(genres_dict[genre], key=lambda x: (-x[1], x[0]))
        answer.extend([idx for idx, _ in sorted_songs[:2]])

    return answer
