def solution(N, stages):
    answer = []
    challenger = [0] * (N + 2)

    # 각 스테이지에 도달한 플레이어 수를 계산
    for stage in stages:
        challenger[stage] += 1

    fails = {}
    total = len(stages)

    # fails에 stage가 key로, 실패율이 value로 저장됨
    for i in range(1, N + 1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total  # 실패율이 계산되어 value로 저장됨
            total -= challenger[i]  # 스테이지를 통과한 인원만큼 남아 있는 인원 줄임

    # 실패율이 높은 순서대로 정렬
    # sorted 함수는 key를 기준으로 정렬하며, reverse=True로 내림차순 정렬
    # sorted 함수에는 딕셔너리의 정렬 결과는 키의 리스트를 반환함
    # fails 딕셔너리의 key는 스테이지 번호, value는 실패율
    answer = sorted(fails, key=lambda x: fails[x], reverse=True)

    return answer
