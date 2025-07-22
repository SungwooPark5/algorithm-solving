from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    completed_days = deque()

    for i, progress in enumerate(progresses):
        completed_day = math.ceil((100 - progress) / speeds[i])
        completed_days.append(completed_day)

    while len(completed_days) != 0:
        count = 1
        day = completed_days.popleft()
        while len(completed_days) != 0 and completed_days[0] <= day:
            count += 1
            completed_days.popleft()
        answer.append(count)

    return answer
