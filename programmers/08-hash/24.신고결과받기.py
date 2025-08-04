def solution(id_list, report, k):
    answer = []
    report_dict = {k: [] for k in id_list}
    reported_num = {k: 0 for k in id_list}
    mailed_num = {k: 0 for k in id_list}

    for r in report:
        rr = r.split(" ")
        if rr[1] not in report_dict[rr[0]]:
            reported_num[rr[1]] += 1
            report_dict[rr[0]].append(rr[1])

    for i, r in report_dict.items():
        for reported in r:
            if reported_num[reported] >= k:
                mailed_num[i] += 1

    answer = list(mailed_num.values())

    return answer
