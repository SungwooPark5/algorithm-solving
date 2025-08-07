def solution(orders, course):
    from itertools import combinations

    # from collection import Counter
    # Counter는 iterable의 요소의 개수를 세어 dictionary 형태로 반환

    answer = []

    for num in course:
        count = {}
        for order in orders:
            # itertools.combinations는 주어진 iterable에서 지정된 길이의 조합을 생성
            # dictionary로 직접 세는 대신 Counter를 이용할 수 있음
            for combi in combinations(order, num):
                combi = tuple(sorted(combi))
                count[combi] = count.get(combi, 0) + 1

        max_num = max(set(count.values()), default=2)
        max_num = max(max_num, 2)

        count = ["".join(combi) for combi, value in count.items() if value == max_num]
        answer += count

    answer.sort()

    return answer
