def solution(n, s):
    answer = []

    if n > s:
        answer.append(-1)
        return answer

    if s % n == 0:
        answer = [s / n] * n
    else:
        answer = [s // n] * (n - s % n)
        answer += [s // n + 1] * (s % n)

    return answer
