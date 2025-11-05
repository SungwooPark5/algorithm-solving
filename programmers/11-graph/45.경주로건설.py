"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/67259#

2차원 그리드에서 직선은 100, 코너는 500의 비용이 추가될 때, 가장 적은 비용으로 경주로를 건설하는 문제
"""

import heapq


def solution(board):
    WIDTH, HEIGHT = len(board[0]), len(board)
    end = (WIDTH - 1, HEIGHT - 1)
    X_DIRECTION = [1, 0, -1, 0]
    Y_DIRECTION = [0, -1, 0, 1]
    min_cost = [
        [[float("inf") for _ in range(4)] for _ in range(WIDTH)] for _ in range(HEIGHT)
    ]
    priority_queue = []

    def is_valid_position(x, y):
        if x > -1 and y > -1 and x < WIDTH and y < HEIGHT:
            return True if board[y][x] == 0 else False
        else:
            return False

    def is_oposite_direction(dir1, dir2):
        return True if (dir1 + 2) % 4 == dir2 else False

    if is_valid_position(1, 0):
        min_cost[0][1][0] = 100
        heapq.heappush(priority_queue, (100, 0, (1, 0)))

    if is_valid_position(0, 1):
        min_cost[1][0][1] = 100
        heapq.heappush(priority_queue, (100, 3, (0, 1)))

    while priority_queue:
        cost, prev_dir, location = heapq.heappop(priority_queue)
        x, y = location

        if location == end:
            return cost

        if cost > min_cost[y][x][prev_dir]:
            continue

        min_cost[y][x][prev_dir] = cost

        for i in range(4):
            next_loc = (location[0] + X_DIRECTION[i], location[1] + Y_DIRECTION[i])
            if not is_valid_position(*next_loc) or is_oposite_direction(prev_dir, i):
                continue
            if prev_dir == i:
                heapq.heappush(priority_queue, (cost + 100, i, next_loc))
            else:
                heapq.heappush(priority_queue, (cost + 600, i, next_loc))
