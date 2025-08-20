"""
책을 보고 직접 다시 푼 코드
문제: https://school.programmers.co.kr/learn/courses/30/lessons/159993
"""

from collections import deque


def find_position(maps, char):
    for y, _ in enumerate(maps):
        for x, _ in enumerate(maps[0]):
            if maps[y][x] == char:
                return x, y
    return None


def is_valid_move(maps, x, y, MAX_COL, MAX_ROW):
    return -1 < x < MAX_ROW and -1 < y < MAX_COL and maps[y][x] != "X"


def solution(maps):
    q = deque()  # BFS를 위한 큐

    MAX_COL, MAX_ROW = len(maps), len(maps[0])
    # visited[y][x][0]은 lever를 당기지 않고 도달한 경우
    # visited[y][x][1]은 lever를 당기고 도달한 경우
    visited = [
        [[False for _ in range(2)] for _ in range(MAX_ROW)] for _ in range(MAX_COL)
    ]

    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]

    sx, sy = find_position(maps, "S")

    visited[sy][sx][0] = True
    q.append((sx, sy, 0, 0))  # position, time, lever 여부

    while q:
        x, y, time, k = q.popleft()

        if maps[y][x] == "E" and k == 1:
            return time

        for i in range(4):
            next_x, next_y = x + nx[i], y + ny[i]

            if not is_valid_move(maps, next_x, next_y, MAX_COL, MAX_ROW):
                continue

            # 현재 위치가 L인 경우, 다시 돌아갈 수도 있기 때문에
            # k의 값을 1로 변경하여 visited가 겹치지 않도록 함
            if maps[y][x] == "L":
                k = 1

            # 방문하지 않은 경우, q에 넣어 다음 라운드에 방문할 수 있도록 함
            # 결과적으로, 가까운 경로부터 방문하여 너비 우선 탐색이 구현됨
            if not visited[next_y][next_x][k]:
                visited[next_y][next_x][k] = True
                q.append((next_x, next_y, time + 1, k))

    return -1


"""
아래의 내용은 책에 있는 풀이를 적은 것으로
처음 시도에서 시간 안에 풀지 못했음
"""

"""
from collections import deque


def is_valid_move(ny, nx, n, m, maps):
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"


def append_to_queue(ny, nx, k, time, visited, q):
    if not visited[ny][nx][k]:
        visited[ny][nx][k] = True
        q.append((ny, nx, k, time + 1))


def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    end_y, end_x = -1, -1

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                q.append((i, j, 0, 0))
                visited[i][j][0] = True
            if maps[i][j] == "E":
                end_y, end_x = i, j

    while q:
        y, x, k, time = q.popleft()

        if y == end_y and x == end_x and k == 1:
            return time

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if not is_valid_move(ny, nx, n, m, maps):
                continue

            if maps[ny][nx] == "L":
                append_to_queue(ny, nx, 1, time, visited, q)
            else:
                append_to_queue(ny, nx, k, time, visited, q)

    return -1
"""
