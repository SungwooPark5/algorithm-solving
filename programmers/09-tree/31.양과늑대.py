"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/92343
이진 트리의 노드에 양과 늑대가 있을 때, 노드를 탐색하면서 양과 늑대를 수집한다.
이때, 양의 수가 늑대의 수보다 많아야만 탐색을 계속할 수 있다.
수집할 수 있는 양의 최대 수를 구하는 문제이다.

dfs를 이용해 푸는 것이 정석이나, 다른 사람들의 풀이를 보면 dfs를 solution 함수 내에
다시 dfs 함수로 정의하여 재귀적으로 풀었다. 아래의 풀이가 비효율적인 부분들이 많으니,
다른 풀이들도 참고해보자.
"""


# stack을 이용한 풀이
def solution(info, edges):

    ships, wolves, node = 1, 0, 0
    max_ships = 1

    tree = {p[0]: [c[1] for c in edges if c[0] == p[0]] for p in edges}
    stack = []
    visited = [False for _ in info]

    print(tree)

    visited[0] = True
    stack.append((node, ships, wolves, visited))

    while stack:
        node, ships, wolves, visited = stack.pop()
        print(node, ships, wolves)
        max_ships = ships if ships > max_ships else max_ships

        try:
            for child in tree[node]:
                v = visited.copy()
                if visited[child]:
                    stack.append((child, ships, wolves, v))
                elif info[child] == 0:
                    v[child] = True
                    stack.append((0, ships + 1, wolves, v))
                elif info[child] == 1:
                    next_wolves = wolves + 1
                    if ships > next_wolves:
                        v[child] = True
                        stack.append((child, ships, next_wolves, v))
        except:
            continue

    return max_ships
