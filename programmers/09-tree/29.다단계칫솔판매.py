def solution(enroll, referral, seller, amount):
    answer = []
    PRICE = 100
    profit_dict = {e: 0 for e in enroll}
    referral_dict = {enroll[i]: r for i, r in enumerate(referral)}

    for i, s in enumerate(seller):
        ref = referral_dict[s]
        profit = amount[i] * PRICE
        distribution = profit // 10
        profit_dict[s] += profit - distribution

        while ref != "-" and distribution > 0:
            profit = distribution
            distribution = distribution // 10
            profit_dict[ref] += profit - distribution
            ref = referral_dict[ref]

    answer = list(profit_dict.values())

    return answer
