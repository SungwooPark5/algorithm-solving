def solution(want, number, discount):
    answer = 0
    want_dict = {}

    # 원하는 상품과 그 수량을 딕셔너리에 저장
    for i, w in enumerate(want):
        want_dict[w] = number[i]

    for i in range(len(discount) - 9):
        want_tmp = want_dict.copy()
        streak = 1
        # 10일 연속으로 원하는 상품이 할인하는 지 확인
        # 다른풀이:discount_10d를 만들어 dict == want_tmp를 통해 확인하는 방법도 있음
        for day in range(10):
            d = discount[i + day]
            if d in want_tmp and want_tmp[d] > 0:
                want_tmp[d] -= 1
                continue
            else:
                streak = 0
                break

        answer += streak

    return answer
