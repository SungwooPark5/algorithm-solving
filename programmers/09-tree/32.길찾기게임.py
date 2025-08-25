"""
문제: https://school.programmers.co.kr/learn/courses/30/lessons/42892#
이진 탐색 트리가 좌표를 토대로 주어졌을 때, 각각 전위 순회와 후위 순회를 수행한 결과를
출력하는 문제.

주의사항
파이썬은 기본적으로 재귀 깊이가 1000으로 설정되어 있어,
재귀 함수를 많이 호출할 경우 아래와 같이 재귀 깊이를 늘려줘야 한다.
"""

import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이를 늘림


def solution(nodeinfo):
    tree = {}
    preorder, postorder, stack = [], [], []

    nodes = [(i + 1, node) for i, node in enumerate(nodeinfo)]
    sorted_nodes = sorted(nodes, key=lambda x: x[1][1], reverse=True)

    root = sorted_nodes[0]
    tree[root[0]] = [None, None]

    def visit_and_set(loc, node):
        if nodeinfo[loc - 1][0] > node[1][0]:
            if tree[loc][0] is None:
                tree[loc][0] = node[0]
                tree[node[0]] = [None, None]
            else:
                visit_and_set(tree[loc][0], node)
        else:
            if tree[loc][1] is None:
                tree[loc][1] = node[0]
                tree[node[0]] = [None, None]
            else:
                visit_and_set(tree[loc][1], node)

    def visit_preorder(node):
        preorder.append(node)
        if tree[node][0] is not None:
            visit_preorder(tree[node][0])
        if tree[node][1] is not None:
            visit_preorder(tree[node][1])

    def visit_postorder(node):
        if tree[node][0] is not None:
            visit_postorder(tree[node][0])
        if tree[node][1] is not None:
            visit_postorder(tree[node][1])
        postorder.append(node)

    for node in sorted_nodes[1:]:
        visit_and_set(root[0], node)

    visit_preorder(root[0])
    visit_postorder(root[0])

    return [preorder, postorder]
