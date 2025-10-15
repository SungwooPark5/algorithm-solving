"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3#

map이 주어지고, 시작 위치가 1,1, 최종 위치가 n,m일 때 최종 위치까지의 최단 거리를 구하는 문제
"""

from collections import deque


def is_valid_loc(maps, loc, end):
    if loc[0] < 0 or loc[1] < 0:
        return False
    if loc[0] > end[0] or loc[1] > end[1]:
        return False
    if maps[loc[1]][loc[0]] == 0:
        return False

    return True


def solution(maps):
    start, end = [0, 0, 1], [len(maps[0]) - 1, len(maps) - 1]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    queue = deque()
    answer = -1

    X_DIR = [1, -1, 0, 0]
    Y_DIR = [0, 0, 1, -1]

    queue.append(start)

    while queue:
        x, y, count = queue.popleft()

        if visited[y][x]:
            continue

        if [x, y] == end:
            answer = count
            break

        visited[y][x] = True
        for i in range(4):
            next_loc = [x + X_DIR[i], y + Y_DIR[i], count + 1]
            if (
                is_valid_loc(maps, next_loc, end)
                and not visited[next_loc[1]][next_loc[0]]
            ):
                queue.append(next_loc)

    return answer
