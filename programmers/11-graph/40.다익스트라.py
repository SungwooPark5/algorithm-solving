"""
문제: 책 422p

문제를 바로 풀지 못해 책을 보고 정리하였음(코드: 424p)
책 보고 더 복습하자.
"""

import heapq
from collections import defaultdict, deque

INF = 999999


def solution(start, numNodes, edges):
    distances = [INF] * numNodes
    visited = [False] * numNodes
    distances[start] = 0
    graph = defaultdict(list)  # list를 default 값으로 가짐

    # O(E)
    for from_node, to_node, weight in edges:
        graph[from_node].append((to_node, weight))

    priority_queue = [(0, start)]

    # O(VlogV)
    while priority_queue:
        # O(logV)
        current_distance, current_node = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue

        visited[current_node] = True

        for neighbor, weight in graph[current_node]:
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


if __name__ == "__main__":
    start1, numNodes1, edges1, result1 = (
        0,
        3,
        [[0, 1, 9], [0, 2, 3], [1, 0, 5], [2, 1, 1]],
        [0, 4, 3],
    )
    answer1 = solution(start1, numNodes1, edges1)
    print(answer1)
    if answer1 == result1:
        print(f"테스트1 통과")
    else:
        print(f"테스트1 실패")

    start2, numNodes2, edges2, result2 = (
        0,
        4,
        [[0, 1, 1], [1, 2, 5], [2, 3, 1]],
        [0, 1, 6, 7],
    )
    answer2 = solution(start2, numNodes2, edges2)
    print(answer2)
    if answer2 == result2:
        print("테스트2 통과")
    else:
        print("테스트2 실패")
