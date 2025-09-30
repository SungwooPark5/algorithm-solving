"""
문제: 책 426p
시간복잡도: O(E+VlogV)

이 문제도 스스로 풀지 못하여 책의 코드를 참조하여 작성하였음
"""

INF = 99999999


def solution(num_vertices, edges, source):
    distances = [INF] * num_vertices
    distances[source] = 0

    graph = [[] for _ in range(num_vertices)]
    for from_vertex, to_vertex, weight in edges:
        graph[from_vertex].append((to_vertex, weight))

    # 정점의 개수 -1 만큼 최소 비용을 갱신
    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # 마지막으로 음의 순환 확인
    for u in range(num_vertices):
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                return [-1]

    return distances


if __name__ == "__main__":
    num_vertices1, edges1, source1, result1 = (
        5,
        [
            [0, 1, 4],
            [0, 2, 3],
            [0, 4, -6],
            [1, 3, 5],
            [2, 1, 2],
            [3, 0, 7],
            [3, 2, 4],
            [4, 2, 2],
        ],
        0,
        [0, -2, -4, 3, -6],
    )
    num_vertices2, edges2, source2, result2 = (
        4,
        [[0, 1, 5], [0, 2, -1], [1, 2, 2], [2, 3, -2], [3, 0, 2], [3, 1, 6]],
        0,
        [-1],
    )

    answer1 = solution(num_vertices1, edges1, source1)
    answer2 = solution(num_vertices2, edges2, source2)

    print(f"응답1: {answer1}")
    print(f"응답l: {answer2}")

    if answer1 == result1:
        print("테스트1 통과")
    else:
        print("테스트1 실패")

    if answer2 == result2:
        print("테스트2 통과")
    else:
        print("테스트2 실패")
