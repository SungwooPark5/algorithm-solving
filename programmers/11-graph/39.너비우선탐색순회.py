"""
문제: 책 420p

graph를 딕셔너리가 아닌, 인접 리스트로 표현하는 것이 더 좋을 수도 있을 것 같다. 그리고 graph_dict 선언 과정에서 O(n)의 시간 복잡도를 필요로 하는 것은 아닌지 한번 점검해보자
"""

from collections import deque


def solution(graph, start):
    answer = []
    visited = set()
    queue = deque([start])
    graph_dict = {}

    for k, v in graph:
        graph_dict[k] = graph_dict.get(k, []) + [v]

    while queue:
        current_node = queue.popleft()

        if current_node in visited:
            continue

        visited.add(current_node)
        answer.append(current_node)

        for next_node in graph_dict.get(current_node, []):
            if next_node not in visited:
                queue.append(next_node)

    return answer


if __name__ == "__main__":
    case1 = [
        [
            (1, 2),
            (1, 3),
            (2, 4),
            (2, 5),
            (3, 6),
            (3, 7),
            (4, 8),
            (5, 8),
            (6, 9),
            (7, 9),
        ],
        1,
    ]
    solution1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    case2 = [[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1]
    solution2 = [1, 2, 3, 4, 5, 0]

    print(f"case1: {solution(*case1)}")
    print(f"case2: {solution(*case2)}")

    if solution1 == solution(*case1):
        print("case1 통과")
    if solution2 == solution(*case2):
        print("case2 통과")
