def solution(k, d):
    answer = 0

    start_point = d - d % k + 1

    for i in range(0, start_point, k):
        num_points = (d**2 - i**2) ** (1 / 2) // k + 1
        answer += num_points

    return answer
