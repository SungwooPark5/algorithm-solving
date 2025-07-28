def solution(participant, completion):
    answer = ""
    completion_dict = {}

    for c in completion:
        completion_dict[c] = completion_dict.get(c, 0) + 1

    for p in participant:
        if p not in completion_dict or completion_dict[p] == 0:
            return p
        else:
            completion_dict[p] -= 1

    return answer


# key in dict는 O(1)의 시간복잡도를 가짐
# key in dict는 key의 존재 여부를 검사
# dict.get(key, default)는 key가 존재하지 않을 때 default 값을 반환
# collections.Counter를 사용하면 더 간단하게 작성할 수 있음
