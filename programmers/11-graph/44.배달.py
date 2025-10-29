"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/12978

K시간 안에 도달할 수 있는 노드의 갯수를 구하는 문제
"""

import heapq
from collections import defaultdict


def solution(N, road, K):
    distances = [float("inf")] * (N + 1)
    distances[1] = 0
    visited = [False] * (N + 1)

    priority_queue = []
    heapq.heappush(priority_queue, (0, 1))

    graph = defaultdict(list)

    for from_node, to_node, d in road:
        graph[from_node].append((to_node, d))
        graph[to_node].append((from_node, d))

    while priority_queue:
        current_dist, node = heapq.heappop(priority_queue)

        if visited[node]:
            continue

        visited[node] = True

        for to_node, edge_weight in graph[node]:
            new_distance = current_dist + edge_weight
            if new_distance < distances[to_node]:
                distances[to_node] = new_distance
                heapq.heappush(priority_queue, (distances[to_node], to_node))

    return sum(1 for d in distances if d <= K)
