"""
문제: 책 417p

스택을 이용해 구현하였으나, 재귀 함수를 이용해서 구현하는 방법도 참고하기
"""


def solution(graph, start):
    answer = []
    visited = set()
    stack = [start]
    graph_dict = {}

    for k, v in graph:
        graph_dict[k] = [v] + graph_dict.get(k, [])

    while stack:
        node = stack.pop()

        answer.append(node)
        visited.add(node)
        for n in graph_dict.get(node, []):
            if n not in visited:
                stack.append(n)

    return answer


if __name__ == "__main__":
    case_1 = ([["A", "B"], ["B", "C"], ["C", "D"], ["D", "E"]], "A")
    case_2 = (
        [["A", "B"], ["A", "C"], ["B", "D"], ["B", "E"], ["C", "F"], ["E", "F"]],
        "A",
    )

    print(f"case 1: {solution(*case_1)}")
    print(f"case 2: {solution(*case_2)}")
